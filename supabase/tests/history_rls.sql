-- Administrator-run integration regression. ALL synthetic data is rolled back.
-- No Google credentials, real users, service-role API keys or permanent test rows.
begin;
do $$
declare
  user_a uuid := gen_random_uuid();
  user_b uuid := gen_random_uuid();
  attempt_a uuid := gen_random_uuid();
  affected integer;
begin
  insert into auth.users (id, aud, role, email, raw_app_meta_data, raw_user_meta_data, created_at, updated_at)
  values (user_a, 'authenticated', 'authenticated', user_a::text || '@ekguru-rls-test.invalid', '{}'::jsonb, '{}'::jsonb, now(), now()),
         (user_b, 'authenticated', 'authenticated', user_b::text || '@ekguru-rls-test.invalid', '{}'::jsonb, '{}'::jsonb, now(), now());
  execute 'set local role authenticated';
  perform set_config('request.jwt.claim.sub', user_a::text, true);
  insert into public.ekguru_attempts (id, user_id, subject_id, test_id, completed_at, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
    values (attempt_a, user_a, 'subject-1', 'test-initial', '2026-09-01T12:00:00.123456Z', 'quiz', 'test-initial', 'Synthetic generic-subject RLS check', 3, null, null, 3, null, null, 0);
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 1 then raise exception 'User A own read failed'; end if;
  if not exists (select from public.ekguru_attempts where id = attempt_a and completed_at = '2026-09-01T12:00:00.123456Z'::timestamptz)
    then raise exception 'Offline completion timestamp not preserved'; end if;

  perform set_config('request.jwt.claim.sub', user_b::text, true);
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 0 then raise exception 'User B can read user A history'; end if;
  delete from public.ekguru_attempts where id = attempt_a;
  get diagnostics affected = row_count;
  if affected <> 0 then raise exception 'Cross-user deletion succeeded'; end if;
  begin
    insert into public.ekguru_attempts (user_id, subject_id, test_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
      values (user_a, 'subject-1', 'test-forbidden', 'quiz', 'test-forbidden', 'Forbidden cross-user insert', 3, null, null, 3, null, null, 0);
    raise exception 'Cross-user insertion unexpectedly succeeded';
  exception when insufficient_privilege then null;
  end;
  begin
    update public.ekguru_attempts set label = 'Forbidden update' where id = attempt_a;
    raise exception 'Immutable attempt update unexpectedly succeeded';
  exception when insufficient_privilege then null;
  end;
  insert into public.ekguru_attempts (user_id, subject_id, test_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
    values (user_b, 'reasoning', 'test-own', 'quiz', 'test-own', 'User B own attempt', 3, null, null, 3, null, null, 0);
  begin
    insert into public.ekguru_attempts (user_id, subject_id, test_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
      values (user_b, 'unsafe/subject', 'test-invalid', 'quiz', 'test-invalid', 'Invalid subject', 3, null, null, 3, null, null, 0);
    raise exception 'Invalid subject slug unexpectedly accepted';
  exception when check_violation then null;
  end;

  perform set_config('request.jwt.claim.sub', user_a::text, true);
  insert into public.ekguru_attempts (user_id, subject_id, test_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
    select user_a, 'subject-' || ((g % 50) + 1), 'test-' || g, 'quiz', 'test-' || g, 'Synthetic scalable history check', 20, null, null, 20, null, null, 0 from generate_series(1, 550) g;
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 551 then raise exception 'Expected all 551 retained A results (no 200 cap), got %', affected; end if;
  select count(distinct subject_id) into affected from public.ekguru_attempts;
  if affected <> 50 then raise exception '50-subject coverage failed: %', affected; end if;
  select count(distinct test_id) into affected from public.ekguru_attempts;
  if affected <> 551 then raise exception '500+ distinct test coverage failed'; end if;
  with first_page as (
    select id, completed_at from public.ekguru_attempts order by completed_at desc, id desc limit 100
  ), second_page as (
    select id, completed_at from public.ekguru_attempts
    where (completed_at, id) < (select completed_at, id from first_page order by completed_at, id limit 1)
    order by completed_at desc, id desc limit 100
  ) select count(distinct id) into affected from (select id from first_page union all select id from second_page) pages;
  if affected <> 200 then raise exception 'Stable timestamp/UUID keyset pagination failed'; end if;
  delete from public.ekguru_attempts where id = attempt_a;
  get diagnostics affected = row_count;
  if affected <> 1 then raise exception 'Own deletion failed'; end if;
  perform set_config('request.jwt.claim.sub', user_b::text, true);
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 1 then raise exception 'Another user history was altered'; end if;
  execute 'reset role';
end;
$$;
rollback;
select 'PASS: 50 subjects, 551 tests/results retained, own reads/inserts/delete, cross-user isolation, immutability, completion timestamps and tied-time keyset paging; all synthetic data rolled back' as result;
