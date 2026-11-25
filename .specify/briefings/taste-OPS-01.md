# Briefing: taste-OPS-01 (issue #14)

## Objective
Scaffold the deployable `apps/taste-engine` skeleton. It needs a FastAPI API, a React PWA shell,
Postgres with Alembic, a worker entrypoint, a compose stack, CI and smoke. The **same image** must
later deploy to Coolify (OPS-02) and Azure Container Apps (OPS-03).

## Context (read these, don't re-derive)
- `specs/projects/taste-engine/architecture.md`: §Overview, §Components & interfaces, and
  §Deployment topology.
- `specs/projects/taste-engine/spec.md`: §Constraints (portability, local-first).
- `specs/projects/taste-engine/research.md`: §Deployment (Coolify compose gotchas, and why we
  don't use SQLite on Azure).

## Acceptance criteria
- AC-OPS01-a: `GET /healthz` returns 200 `{"status":"ok"}`. `GET /readyz` returns 200 only when
  the DB is reachable and migrations are at head. — level: integration — environment: cloud-linux —
  test: `apps/taste-engine/tests/integration/test_health.py` (tbd)
- AC-OPS01-b: `GET /v1/openapi.json` is served, and `GET /` serves the built PWA shell (a title
  plus an empty Discover page) from the same origin. — level: integration — environment:
  cloud-linux — test: `apps/taste-engine/tests/integration/test_static_and_openapi.py` (tbd)
- AC-OPS01-c: `docker compose -f apps/taste-engine/compose.yaml up` works with only
  `.env.example` values. It starts `postgres`, a one-shot `migrate` (`restart: "no"`), `api`
  and `worker`. `TASTE_SMOKE_BASE_URL=http://localhost:8000 bash scripts/smoke.sh` passes.
  — level: smoke — environment: cloud-linux — test: CI job `compose-smoke` in
  `.github/workflows/taste-engine.yml` (tbd)
- AC-OPS01-d: Settings load only from env vars: `DATABASE_URL`, `AUTH_MODE`, `PUBLIC_BASE_URL`,
  `CLOUD_AI_CONSENT` (default `false`), `LLM_BASE_URL`, `STT_URL`, `AVAILABILITY_PROVIDER`,
  `AVAILABILITY_API_KEY`, `CATALOG_USER_AGENT` and `REGION` (default `US`). Missing required values
  fail fast with a clear message. — level: unit — environment: cloud-linux — test:
  `apps/taste-engine/tests/unit/test_settings.py` (tbd)
- AC-OPS01-e: CI runs ruff, mypy, pytest (with a Postgres service), web lint/typecheck/vitest and
  compose-smoke on `pull_request`, `push` to main **and `merge_group`**. On main it pushes
  `ghcr.io/kixantrix/taste-engine:<sha>` and `:main`. — level: smoke — environment: cloud-linux —
  test: the workflow itself plus `python -m tools.validators.check_merge_queue`.

## Scope
- Touch:
  - `apps/taste-engine/**` (new): `pyproject.toml` (uv or pip; Python 3.12), `src/taste_engine/**`,
    `alembic/**`, `tests/**`, `web/**` (Vite + React + TS), `Dockerfile` (multi-stage: node build →
    python runtime, non-root, `HEALTHCHECK`), `compose.yaml`, `.env.example`, `README.md`.
  - `.github/workflows/taste-engine.yml` (new).
  - `scripts/smoke.sh` and `scripts/smoke.ps1`: add an **opt-in** taste-engine section gated on
    `TASTE_SMOKE_BASE_URL`, mirroring the existing `KERRIGAN_SMOKE_DASHBOARD` pattern. It checks
    `/healthz`, `/readyz` and `/v1/openapi.json`. The default behaviour must not change.
  - `pnpm-workspace.yaml`, only if needed to include `apps/taste-engine/web`.
- Read-only: `specs/projects/taste-engine/**`, `apps/kerrigan-dashboard/**` (for tooling
  conventions), `tools/validators/**`.
- Out of scope:
  - Domain models, importers and auth (CORE-01/02).
  - Coolify magic variables or Azure Bicep (OPS-02/03).
  - STT/LLM containers.
  - Any TMDB usage (decision D1: no TMDB).
  - Publishing host ports other than `8000` for local dev.

## Prior decisions
- Modular monolith: one image with `api` and `worker` roles selected by command. —
  architecture.md §Tradeoffs.
- Postgres everywhere. SQLite is allowed only in unit tests. — architecture.md §Tradeoffs.
- The PWA is built into the image and served by FastAPI from the same origin, with no CORS. —
  research.md D6.
- Job queue is Postgres-backed. A worker loop stub is enough for now. — architecture.md
  §Components.
- Compose must run under plain `docker compose`. Use `${VAR:-default}` and `${VAR:?}` for
  required values. Don't use Coolify-only `SERVICE_*` variables yet. — research.md §Deployment.

## Relevant skills (preload)
- smoke-test
- test-ladder
- e2e-test (Playwright isn't required yet; just leave `web/tests/e2e/` ready)

## Test commands
- unit: `cd apps/taste-engine && pytest tests/unit -q`
- integration: `cd apps/taste-engine && pytest tests/integration -q` (needs `DATABASE_URL` for
  Postgres)
- web: `pnpm -C apps/taste-engine/web lint && pnpm -C apps/taste-engine/web test`
- smoke: `docker compose -f apps/taste-engine/compose.yaml up -d --build && TASTE_SMOKE_BASE_URL=http://localhost:8000 bash scripts/smoke.sh`
- repo: `python -m tools.validators.check_artifacts && bash scripts/smoke.sh`

## Routing rule matched
R-cloud-default: standard code and CI scaffolding with no device, OS or secret needs.
GHCR push uses `GITHUB_TOKEN`.

## Budget
- max_turns: 60
- max_premium_requests: 30
