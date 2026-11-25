# Acceptance tests: taste-engine

Each test maps to an AC in [`spec.md`](./spec.md) and to its owning task in [`tasks.md`](./tasks.md).
Test paths are proposals; the owning task creates them.

- `apps/taste-engine/tests/unit/**` and `tests/integration/**`: pytest
- `apps/taste-engine/web/tests/e2e/**`: Playwright
- `scripts/smoke.sh`: deploy smoke against `SMOKE_BASE_URL`

## AC-01: Idempotent import

- [ ] **Given** fixture exports for Letterboxd, IMDb, Netflix and Trakt **When** each is imported twice **Then** the event count and content hashes match the first import, and unmatched titles appear once in the review queue (CORE-01 · integration · cloud-linux · `tests/integration/test_import_idempotent.py`)

## AC-02: Export/restore round-trip

- [ ] **Given** a household with events, observations and corrections **When** it is exported, the database is wiped, and the export is restored **Then** a second export is byte-equal in canonical JSON (CORE-02 · integration · cloud-linux · `tests/integration/test_export_roundtrip.py`)

## AC-03: Viewer deletion

- [ ] **Given** two viewers with events **When** viewer A is deleted **Then** no rows reference A in the event, observation, feature or exposure tables, and B's recommendations are unchanged (CORE-02 · integration · cloud-linux · `tests/integration/test_delete_viewer.py`)

## AC-04: Explainable ranking

- [ ] **Given** a viewer with ≥10 rated titles **When** `POST /v1/recommendations` is called **Then** every returned title is unseen and carries ≥1 explanation whose evidence ids resolve to that viewer's events (ML-02 · integration · cloud-linux · `tests/integration/test_recommendations_explained.py`)

## AC-05: Legitimate launch handoff

- [ ] **Given** a title with a vendor offer **When** the user clicks *Watch on X* **Then** a new tab opens to the vendor-supplied provider URL with `noopener`, and an exposure event is logged (UX-02 · e2e · cloud-linux · `web/tests/e2e/launch.spec.ts`)
- [ ] **Given** an offer without a deep link **When** the user launches it **Then** the fallback chain is used (provider search URL, then provider home page) (AV-01 · unit · cloud-linux · `tests/unit/test_launch_fallback.py`)
- [ ] **Given** the provider matrix **When** DISC-03 is re-run **Then** the results are recorded with last-tested dates (DISC-03 · scenario · manual-human · `research/disc-03-launch-matrix.md`)

## AC-06: Reviewable feedback changes ranking

- [ ] **Given** the transcript "loved the politics, hated the contrived drama" for title X **When** it is submitted **Then** tentative observations (`political_intrigue`+, `contrived_conflict`−, scope=title) are returned and not yet applied (ML-03 · integration · cloud-linux · `tests/integration/test_feedback_extraction.py`, LLM mocked)
- [ ] **Given** tentative observations **When** they are accepted **Then** the next recommendation list differs and cites them; **When** they are undone **Then** the ranking reverts (ML-03 · integration · cloud-linux · `tests/integration/test_feedback_accept_undo.py`)
- [ ] **Given** a browser with fake mic input **When** push-to-talk is used **Then** a recording indicator shows and the review panel appears (UX-01 · e2e · cloud-linux · `web/tests/e2e/voice.spec.ts`)

## AC-07: Privacy defaults

- [ ] **Given** default config **When** voice feedback is processed **Then** no audio file remains on disk, and no outbound request goes to a host outside the allow-list (PRIV-01 · integration · cloud-linux · `tests/integration/test_privacy_defaults.py`)
- [ ] **Given** `CLOUD_AI_CONSENT=false` and `LLM_BASE_URL` pointing at a cloud host **When** extraction runs **Then** the request is refused with a consent error (PRIV-01 · unit · cloud-linux · `tests/unit/test_consent_guard.py`)

## AC-08: Dual-host deploy

- [ ] **Given** image tag T **When** it is deployed via Coolify compose **Then** `scripts/smoke.sh` passes against the Coolify URL (OPS-01 · smoke · local-attested-coolify · `scripts/smoke.sh`)
- [ ] **Given** the same tag T **When** it is deployed via `azd up` **Then** `scripts/smoke.sh` passes against the ACA URL (OPS-02 · smoke · local-attested-azure · `scripts/smoke.sh`)
- [ ] **Given** `compose.yaml` **When** it runs under plain `docker compose up` in CI **Then** smoke passes (T-SCAFFOLD · smoke · cloud-linux · `.github/workflows/taste-engine.yml`)

## AC-09: Planner correctness

- [ ] **Given** fixtures with overlapping providers and a budget **When** a plan is computed **Then** no title is counted twice, the total cost is at most the budget, and the scheduled hours are at most the capacity, matching the hand-calculated expected plans (PLAN-01 · unit · cloud-linux · `tests/unit/test_planner_fixtures.py`)
