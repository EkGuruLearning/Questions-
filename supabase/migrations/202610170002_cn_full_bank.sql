-- The CN app also offers the entire 1,554-question bank; paper rooms remain <=300.
begin;
alter table public.ekguru_attempts drop constraint ekguru_attempts_total_check;
alter table public.ekguru_attempts add constraint ekguru_attempts_total_check
  check (total between 1 and 2000 and (kind = 'cn' or total <= 300));
commit;
