-- Private, bounded practice history. Public papers and question banks stay in Git.
-- Uses the user's JWT + publishable key, never a service-role key in the app.
begin;

create table public.ekguru_attempts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  kind text not null check (kind in ('cn', 'paper')),
  paper_id text not null check (paper_id ~ '^[A-Za-z0-9_.-]{1,128}$'),
  label text not null check (char_length(btrim(label)) between 1 and 200),
  total integer not null check (total between 1 and 300),
  correct integer,
  wrong integer,
  unanswered integer not null check (unanswered between 0 and total),
  score numeric(9,3),
  max_score numeric(9,3),
  duration_seconds integer not null check (duration_seconds between 0 and 604800),
  details jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  constraint ekguru_score_consistency check (
    (correct is null and wrong is null and score is null and max_score is null)
    or (correct is not null and wrong is not null and score is not null and max_score is not null
      and correct >= 0 and wrong >= 0 and correct + wrong + unanswered <= total
      and max_score > 0 and max_score <= 30000 and score between -30000 and max_score)
  ),
  constraint ekguru_small_details check (jsonb_typeof(details) = 'object' and octet_length(details::text) <= 20000)
);

create index ekguru_attempts_user_recent on public.ekguru_attempts (user_id, created_at desc, id);
alter table public.ekguru_attempts enable row level security;
alter table public.ekguru_attempts force row level security;

revoke all on public.ekguru_attempts from anon, authenticated;
grant select, delete on public.ekguru_attempts to authenticated;
grant insert (id, user_id, kind, paper_id, label, total, correct, wrong, unanswered,
  score, max_score, duration_seconds, details) on public.ekguru_attempts to authenticated;

create policy ekguru_read_own on public.ekguru_attempts for select to authenticated
  using ((select auth.uid()) = user_id);
create policy ekguru_insert_own on public.ekguru_attempts for insert to authenticated
  with check ((select auth.uid()) = user_id);
create policy ekguru_delete_own on public.ekguru_attempts for delete to authenticated
  using ((select auth.uid()) = user_id);
-- Intentionally no UPDATE policy. A submitted attempt is immutable.

create function public.ekguru_trim_history() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  -- Keep storage bounded without a paid scheduler or an artificial keep-alive job.
  perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtextextended(new.user_id::text, 17));
  delete from public.ekguru_attempts where user_id = new.user_id and id in (
    select id from public.ekguru_attempts where user_id = new.user_id
    order by created_at desc, id desc offset 200
  );
  return new;
end;
$$;
revoke all on function public.ekguru_trim_history() from public, anon, authenticated;
create trigger ekguru_bounded_history after insert on public.ekguru_attempts
  for each row execute function public.ekguru_trim_history();

comment on table public.ekguru_attempts is
  'Self-practice results, not proctored scores or a competitive leaderboard. Latest 200 per user.';
commit;
