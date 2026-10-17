# Google login + Test Room — setup & maintenance

## What is ready

- Separate **free-plan Supabase project**, `EkGuru Questions`, Mumbai (`ap-south-1`), ref `byinrfmonsqfkoxejhgn`.
- Separate **Vercel project**, `ekguru-questions`, ID `prj_1kdFq22FVdir3TWOQcILikOtcmeL`.
- Reserved production origin: `https://ekguru-questions.vercel.app`. **No production deployment has been created yet.**
- DB migrations in `supabase/migrations/` have already been applied to this new project. Existing unrelated projects were not changed.
- Vercel server environment configured: `SUPABASE_URL`, `SUPABASE_PUBLISHABLE_KEY`, `SESSION_SECRET`, `APP_ORIGIN`.
- **Owner action still required:** create/enable the Google OAuth provider. Connecting Supabase/Vercel does not create a Google Cloud OAuth client. No password/client secret should be pasted in chat or committed to Git.
- Vercel's GitHub integration does **not** currently have permission for `EkGuruLearning/Questions-`. Grant that repository access and link this existing project for automatic deployment. The connector's direct-upload deployment was also attempted on 2026-10-17, but Vercel rejected it before building: `projectSettings` is required, and this connector does not expose that field. Follow-up deployment listing confirmed that no deployment was created. Do not create another paid project.

## 1. Enable Google once (owner, in the dashboards)

1. In **Google Cloud Console → Google Auth Platform / APIs & Services → Credentials**, create a **Web application OAuth client**.
2. Configure the consent screen with only basic OpenID, email and profile scopes. If the app is in Testing, add your Google account to Test users; publish the consent app appropriately before allowing everyone to sign in. Follow any Google verification requirements shown there.
3. Authorized JavaScript origin (if requested):
   ```text
   https://ekguru-questions.vercel.app
   ```
4. Authorized redirect URI — **this is the Supabase callback, not the Vercel callback**:
   ```text
   https://byinrfmonsqfkoxejhgn.supabase.co/auth/v1/callback
   ```
5. Open [Supabase → Authentication → Sign In / Providers](https://supabase.com/dashboard/project/byinrfmonsqfkoxejhgn/auth/providers), enable **Google**, and paste the Google Client ID and Client Secret **there only**. Leave nonce checks enabled. Save.
6. In Supabase Authentication → URL Configuration, Site URL is:
   ```text
   https://ekguru-questions.vercel.app
   ```
   Allowed redirect URLs are restricted to this application's callback, including the state query:
   ```text
   https://ekguru-questions.vercel.app/api/auth/callback
   https://ekguru-questions.vercel.app/api/auth/callback?state=*
   http://localhost:8000/api/auth/callback
   http://localhost:8000/api/auth/callback?state=*
   ```
   Localhost entries are only needed for local OAuth development; remove them if unused. There is intentionally no catch-all allowlist for other people's Vercel previews.
7. Open `/subjects/account/index.html`, click **Continue with Google**, complete Google's official consent screen, then run a test. Check that the result appears in My Account after reload. A disabled provider is shown honestly as **setup pending**; guest practice continues to work. Provider-status cache lasts at most 60 seconds.

Until step 5 is done, a live Google sign-in cannot be completed or claimed as tested. Local security tests use a mocked auth server, never a fake logged-in production account.

## 2. Local development

```bash
npm ci
cp .env.example .env.local
# Fill .env.local from your own project's server configuration, never a service-role key.
# Generate SESSION_SECRET independently with the command in .env.example.
npm run dev
# Open http://localhost:8000/subjects/test-room/index.html
```

`npm run dev` runs one Node server, binding `0.0.0.0:8000`. It serves the public allowlist and `/api/` on the **same origin**, supports `/Questions-/` and PDF byte ranges, and accepts the Arena preview host without iframe blocks. Browser code never calls another localhost backend.

For a guest-only preview or an environment that cannot reach Supabase:

```bash
EKGURU_DISABLE_AUTH=true npm run dev
```

`EKGURU_DISABLE_AUTH` is a **local preview** switch only. The production function does not read it. The dev runtime response uses a `same-origin` marker; the static runtime file points to the real HTTPS Vercel origin. GitHub Pages does not support server functions or HttpOnly OAuth cookies, so its login button opens Vercel; guest tests/PDFs work directly on Pages. Cookies are not shared between those different domains.

## 3. Add old papers — no code change, no OCR service

Put the PDF here, preserving the original exam/paper numbering:

```text
content/previous-year-papers/<exam>/<year>/My-Paper.pdf
```

Then run:

```bash
npm run build:content
# = build_practice.py → build_catalog.py → build_pages.py → build_site_routes.py
python3 tools/validate_site.py
npm test
npm run build
```

Every uploaded question PDF gets a Test Room card and a **Practice as test** link in its folder. A scanned PDF works as-is: read one page at a time, choose responses on the OMR sheet, mark/revisit/clear, time the attempt, submit and review. Only the selected PDF and current canvas page are rendered. Source material stays in Git; it does not consume database storage or a paid OCR quota.

**Without a digital key:** confirm the question count/options in the setup form. The result shows attempted/skipped counts and **Unscored**, not invented marks, correctness or percentages. Time/marking defaults are configurable **practice defaults**, not assertions about official exam rules.

### Optional digital key / bilingual labels

Keep build metadata **outside** the student `content/` tree. Mirror the PDF's path under:

```text
data/practice/papers/<exam>/<year>/My-Paper.paper.json
```

Example (replace both hashes with actual file hashes; do not copy an old paper's key):

```json
{
  "schema_version": 1,
  "id": "my-exam-2024-paper-1",
  "title": "My Exam 2024 — Paper 1",
  "title_hi": "मेरी परीक्षा 2024 — पेपर 1",
  "question_count": 3,
  "options_count": 4,
  "duration_minutes": 120,
  "marks": 1,
  "negative_marks": 0,
  "paper_sha256": "SHA256_OF_QUESTION_PDF",
  "key_pdf": "content/previous-year-papers/<exam>/<year>/My-Paper-Answer-Key.pdf",
  "key_sha256": "SHA256_OF_KEY_PDF",
  "key_note": "Provided practice key; check the latest official final key before relying on the score.",
  "answer_key": { "1": "C", "2": ["A", "B"], "3": "DROP" }
}
```

- Options map `A=1, B=2, C=3, D=4, E=5`. Multiple accepted answers use an array; `DROP` excludes a question from the denominator. Missing entries stay ungraded. Partial keys score **only keyed questions**.
- If an exam explicitly has “5. Question not attempted”, use `"options_count": 5, "skip_option": "E"`. Otherwise E is an ordinary fifth answer. There is no automatic assumption that option 5 is always a skip.
- Key-bearing metadata requires the matching question PDF SHA-256. If a linked key hash or question hash changes, the build stops until a human reviews the mapping. File hash command: `sha256sum path/to/file.pdf`.
- A key is always labelled **provided / not independently official-final-key verified** in this v1 room. This does not weaken the existing CN bank's official-evidence gate.
- RPSC Programmer 2024 Paper 1 has a repository-key transcription, **not a newly verified official key**. Q3's key conflicts with the question (500 minus 70 is 430, not the supplied 324) and Q5's reprinted table is incomplete; both are intentionally ungraded. 98/100 items have a provided key. Existing PDFs have not been rewritten.
- The two uploaded BCI 2022 scanned papers have no digital key or verified count; they are available as unscored practice, with count confirmed by the student.

## 4. Sessions, privacy, boundaries

- Server-only Google OAuth **PKCE + random state**. The short-lived OAuth flow cookie and session cookies are encrypted/authenticated with AES-256-GCM, with separate purposes and fresh IVs. Cookies are chunked below browser size limits.
- HTTPS cookies use `__Host-`, `HttpOnly`, `Secure`, `SameSite=Lax`, `Path=/`, no Domain. Access/refresh tokens are **never** returned to JS or saved in local/session storage. Only explicitly opted-in localhost HTTP development can omit Secure.
- Session cookies persist up to **30 days**, with access-token refresh when needed. Google revocation, browser cookie deletion, provider policy, rotating the session secret or an auth outage can require a new login; there is no “never expires” token promise.
- Writes require exact `APP_ORIGIN` + a CSRF header. Each history request also carries the expected non-secret user ID. The server verifies `/auth/v1/user`, derives the actual ID from that response, rejects account-switch races, and sends the user's JWT to Postgres. Browser user IDs are never authorization.
- **No service-role key.** Postgres RLS allows only SELECT/INSERT/DELETE of the authenticated user's own immutable attempts. The insertion trigger retains the latest 200 per user; the UI fetches the latest 50. Users can delete individual results; deleting the auth user cascades history deletion.
- Google identity/email stays in Supabase Auth. No extra profile table, tracking/advertising cookies or analytics SDK has been added.
- Old-paper drafts survive reload for up to 7 days on the same browser. Wall-clock deadlines are recomputed on resume; closing a tab does not pause time. Updated paper/key fingerprints invalidate old drafts. Review marks do not suppress selected answers at submission.
- The latest paper result is local and downloadable as JSON. Cloud sync only applies to attempts **started while signed in to that same account**. Guest drafts/history are never silently uploaded to a later/different login. Local browser history/drafts are not a multi-user vault; shared-device users should clear site data as well as log out.
- Offline cloud writes have idempotent UUIDs and an owner-scoped local outbox (max 20 pending attempts), retried on Online / Sync. Storage-disabled browsers retain a volatile outbox for the current tab and show a warning. Logged-out users' pending outbox is cleared from that browser.
- CN preserves its existing local saved-question/result behaviour. New signed-in CN summaries can also sync; for sets over 150 questions the cloud record omits individual answers to keep requests small. The full CN bank still works (up to 2,000 supported in history), while PDF rooms are capped at 300.
- These are **self-practice** scores: questions/keys are public and results are client-computed, not proctored or suitable for a trusted competitive leaderboard.

## 5. Deployment / speed / free-tier reality

```bash
npm ci
npm run build:content
npm run build
```

`tools/build_web.mjs` exports allowlisted public files into ignored `public/`, minifies own JS/CSS/HTML/JSON, and precompresses text at **Brotli quality 11 / gzip level 9**. It also emits `.vercel/output/` Build Output API v3 with a tiny Node 22 server function in `bom1` (Mumbai). Vercel's CDN negotiates transfer compression; the preview server can serve the generated `.br`/`.gz` variants. Hashed question chunks get immutable caching; other files revalidate. Auth/user API responses are always private/no-store. PDFs/images are not destructively downsampled for a misleading compression claim.

No React/Next runtime, browser auth SDK, fonts CDN, ORM or continuously running paid server has been introduced. The Python scripts run at build time, never on a student request. Rewriting the static app in Rust/C++ would not remove network latency or make Google/DB operations the “fastest ever”; small payloads, static delivery and lazy PDF/chunk loading are the practical optimizations.

For automatic Vercel updates: grant the Vercel GitHub App access to **EkGuruLearning/Questions-** and connect it to this existing Vercel project. Build is `npm run build`, install is `npm ci`; `npm run build` automatically runs `build:content` first, so newly uploaded papers are discovered during each deployment. The generated HTML/manifests can also be refreshed locally with `npm run build:content`. Do not expose `.env.local` or use a service-role key.

**Publish from the Vercel dashboard:** grant the Vercel GitHub App access to this repository, connect it in the existing project's **Settings → Git**, then deploy the reviewed source. After merging the feature PR, deploy `main` for the regular production site. Keep install `npm ci`, build `npm run build`, output `public`, and Node 22 (or newer). Server environment variables have already been configured; do not paste secrets into a build command or source file. Existing GitHub Pages still serves `main` until the PR is merged.

`tools/vercel_snapshot_bootstrap.mjs` is an **optional, not end-to-end deployment-verified** fallback for a capable deployment client. It takes only a public, immutable commit SHA in `EKGURU_SOURCE_SHA`, fetches that GitHub codeload snapshot and runs the locked build. The supplied connector could not submit the required deployment `projectSettings`, so this fallback did not publish a site here. It stores no GitHub token or Google secret in source and does not automatically track future pushes.

The GitHub Actions workflow verifies PRs and publishes a freshly generated static `public/` on pushes to main (enable **Settings → Pages → Source: GitHub Actions** once). It does not deploy a backend or magically provision a Google OAuth app.

**No lifetime guarantee:** free plans have storage, bandwidth, function, fair-use and inactivity limits and providers can change terms. Supabase projects may pause after inactivity; restore them in the dashboard if that happens. No artificial keep-alive cron, paid plan or entitlement bypass is used. Public PDFs/question banks and schema remain in Git; private history stays in the database, not a public GitHub “database”. Download results/back up data as needed. A free static fallback keeps guest practice usable when login/database is unavailable.

## 6. Verification

```bash
npm test
python3 tools/build_practice.py --check
python3 tools/read_structure.py --check
python3 tools/run_release_checks.py

# Optional real browser tooling (not app runtime dependencies):
npm install --prefix .cache/browser-deps puppeteer-core@24.16.0 @sparticuz/chromium@138.0.2 jsdom@26.1.0
NODE_PATH="$PWD/.cache/browser-deps/node_modules" node tests/mobile/room_account_check.cjs
```

The browser regression exercises 360/390/768/951/1280px, real local PDFs, OMR, failure/retry/cancellation, bounded-canvas zoom, clear/review/palette, reload/resume, expiry/auto-submit, truthful unscored results, quick CN presets, and **mocked** account/history/offline/logout/storage-failure UI. PDF.js worker-termination notices caused by the intentional network-abort test are classified separately; unrelated errors still fail. This is not a claim of completing Google's live consent flow. If the host lacks NSS/NSPR, use system Chromium or unpack the optional Chromium package's `al2023.tar.br` libraries into an ignored cache and set `LD_LIBRARY_PATH`; no browser binaries/libraries are committed.

Verified on 2026-10-17: all 24 local release gates passed against the minified production export (including all optional browser checks), 41 Node tests passed, 79 Python tests passed, and the GitHub Verify portal push workflow passed. Supabase's forced RLS/policies were independently queried, and `supabase/tests/history_rls.sql` passed own-user read/insert, cross-user read/insert/delete denial, immutable results and 200-result retention. Its synthetic users/results were rolled back. The callback allowlist includes the explicit state-query patterns above. Live Google consent, physical devices, and a public Vercel deployment remain unverified.
