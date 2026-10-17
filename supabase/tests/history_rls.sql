-- Integration regression for a disposable/new Supabase database.
-- Run as the project database administrator. All synthetic data is rolled back.
-- Never uses real users, OAuth credentials, tokens or a service-role API key.
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
  insert into public.ekguru_attempts (id, user_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
    values (attempt_a, user_a, 'paper', 'rls-test', 'Synthetic RLS check', 3, null, null, 3, null, null, 0);
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 1 then raise exception 'User A own read failed'; end if;

  perform set_config('request.jwt.claim.sub', user_b::text, true);
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 0 then raise exception 'User B can read user A history'; end if;
  delete from public.ekguru_attempts where id = attempt_a;
  get diagnostics affected = row_count;
  if affected <> 0 then raise exception 'Cross-user deletion succeeded'; end if;
  begin
    insert into public.ekguru_attempts (user_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
      values (user_a, 'paper', 'rls-test', 'Forbidden cross-user insert', 3, null, null, 3, null, null, 0);
    raise exception 'Cross-user insertion unexpectedly succeeded';
  exception when insufficient_privilege then null;
  end;
  begin
    update public.ekguru_attempts set label = 'Forbidden update' where id = attempt_a;
    raise exception 'Immutable attempt update unexpectedly succeeded';
  exception when insufficient_privilege then null;
  end;
  insert into public.ekguru_attempts (user_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
    values (user_b, 'paper', 'rls-test', 'User B own attempt', 3, null, null, 3, null, null, 0);

  perform set_config('request.jwt.claim.sub', user_a::text, true);
  insert into public.ekguru_attempts (user_id, kind, paper_id, label, total, correct, wrong, unanswered, score, max_score, duration_seconds)
    select user_a, 'paper', 'rls-test', 'Synthetic retention check', 3, null, null, 3, null, null, 0 from generate_series(1, 201);
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 200 then raise exception 'Expected 200 retained results for A, got %', affected; end if;
  perform set_config('request.jwt.claim.sub', user_b::text, true);
  select count(*) into affected from public.ekguru_attempts;
  if affected <> 1 then raise exception 'Retention deleted another user history'; end if;
  execute 'reset role';
end;
$$;
rollback;
select 'PASS: own reads/inserts, cross-user isolation, immutable results and 200-result retention; all synthetic data rolled back' as result;
