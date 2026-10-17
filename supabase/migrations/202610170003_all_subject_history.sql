-- All subjects/tests share the same private attempt store. No automatic pruning.
-- Apply after migrations 001/002; preserves every existing result and RLS policy.
begin;
alter table public.ekguru_attempts add column subject_id text;
alter table public.ekguru_attempts add column test_id text;
alter table public.ekguru_attempts add column completed_at timestamptz not null default now();
update public.ekguru_attempts set completed_at = created_at;
update public.ekguru_attempts set
  subject_id = case when kind = 'cn' then 'computer-network' else 'previous-year-papers' end,
  test_id = paper_id;
alter table public.ekguru_attempts alter column subject_id set not null;
alter table public.ekguru_attempts alter column test_id set not null;
alter table public.ekguru_attempts add constraint ekguru_subject_slug
  check (subject_id ~ '^[a-z0-9][a-z0-9_.-]{0,95}$');
alter table public.ekguru_attempts add constraint ekguru_test_slug
  check (test_id ~ '^[A-Za-z0-9_.-]{1,128}$');
alter table public.ekguru_attempts drop constraint ekguru_attempts_kind_check;
alter table public.ekguru_attempts add constraint ekguru_attempts_kind_check
  check (kind in ('cn', 'paper', 'quiz'));
alter table public.ekguru_attempts drop constraint ekguru_attempts_total_check;
alter table public.ekguru_attempts add constraint ekguru_attempts_total_check
  check (total between 1 and 2000 and (kind <> 'paper' or total <= 300));
grant insert (subject_id, test_id, completed_at) on public.ekguru_attempts to authenticated;
drop trigger if exists ekguru_bounded_history on public.ekguru_attempts;
drop function if exists public.ekguru_trim_history();
drop index public.ekguru_attempts_user_recent;
create index ekguru_attempts_user_recent on public.ekguru_attempts (user_id, completed_at desc, id desc);
create index ekguru_attempts_subject_recent on public.ekguru_attempts (user_id, subject_id, completed_at desc, id desc);
create index ekguru_attempts_subject_test_recent on public.ekguru_attempts (user_id, subject_id, test_id, completed_at desc, id desc);
create index ekguru_attempts_test_recent on public.ekguru_attempts (user_id, test_id, completed_at desc, id desc);
comment on table public.ekguru_attempts is
  'Immutable own-user self-practice results across all subjects/tests. No automatic 200-result pruning; paginated summaries. Provider storage quotas still apply.';
commit;
