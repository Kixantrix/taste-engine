# Test plan: taste-engine

Strategy follows [`docs/test-strategy.md`](../../../docs/test-strategy.md): the test level and the
environment are chosen separately for each AC.

## Levels

- **Unit (pytest, Vitest):** importer parsers, idempotency keys, fallback chain, consent guard,
  planner fixtures, ranking math, and React components.
- **Integration (pytest + Postgres service container):**
  - API routes against a real Postgres.
  - External vendors (Wikidata, TVmaze, MotN, STT, LLM) replaced with recorded fixtures (`respx`/VCR-style).
    No live API calls in CI.
- **Offline ML evaluation (pytest marker `eval`):**
  - Runs the temporal-split benchmark on committed fixtures.
  - Fails if the result regresses past a tolerance against the stored baseline report.
- **E2E (Playwright, headless Chromium):** the compose stack runs in CI and Playwright drives
  import → discover → launch → react. Fake mic input comes from
  `--use-fake-device-for-media-stream`.
- **Smoke (`scripts/smoke.sh`):** `/healthz`, `/v1/openapi.json`, and an authenticated
  `GET /v1/profiles/me`, run against any `SMOKE_BASE_URL`. Gates merges in CI on plain Compose;
  attested runs cover Coolify and ACA.
- **Scenario (manual-human):** the provider launch matrix (DISC-03) and real-voice sessions
  on household hardware.

## Tooling

- Python: pytest, pytest-asyncio, respx, hypothesis (importer fuzzing), ruff, mypy.
- Web: Vitest, Testing Library, Playwright, ESLint, `tsc --noEmit`.
- CI: a `.github/workflows/taste-engine.yml` workflow (created by T-SCAFFOLD) with lint, unit,
  integration (Postgres service), e2e (compose) and an image build/push to GHCR. It must also
  run on `merge_group` per `check_merge_queue.py`.

## Risk areas / focus

| Risk | Focus | Tests |
|---|---|---|
| Duplicate or lost evidence on re-import | importers | Hypothesis-based fuzzing of row order and duplicates; AC-01 |
| Privacy regressions (egress, audio retention) | voice, consent | AC-07; a network allow-list fixture fails on unexpected hosts |
| Ranking leakage or overfitting | taste/eval | Temporal split asserting no future events in training; baseline comparison |
| Vendor schema drift | catalog/availability | Contract tests on recorded fixtures, plus a weekly live canary job (non-blocking) |
| Host divergence between Coolify and Azure | deploy | The same image tag is smoke-tested on both (AC-08) |
| Mistaken generalization from voice | extraction | Labeled ambiguous/conditional set; tracks the mistaken-generalization rate |
