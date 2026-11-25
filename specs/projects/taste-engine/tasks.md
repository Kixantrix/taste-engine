# Tasks: taste-engine

Each task ends with green CI and has explicit "done" criteria. The Routing column cites
[`delegation-rubric`](../../../.github/skills/delegation-rubric/SKILL.md).

## Milestone 0 — Discovery

- [ ] Task: DISC-01 Upstream shell audit (PenguWatch, Sofa, Findarr)
  - Done when: `research/disc-01-upstream.md` records the pinned commit, deploy commands, import
    results, API surface (whether it can accept external scores), auth/security posture, and a
    D4 recommendation.
  - Links: research.md §Upstream; dossier §3
  - Routing: R-local.human-judgment (hands-on UX evaluation with household data)
- [ ] Task: DISC-02 License & data-terms review
  - Done when: an SPDX table for the candidates is written; the TMDB, MotN, Watchmode and
    MovieLens terms are summarized with the clauses quoted; a TMDB clarification email is drafted;
    and D1/D2 options are written up for the human to decide.
  - Links: research.md §Data, D1, D2
  - Routing: R-cloud-default
- [ ] Task: DISC-03 Provider web-launch matrix
  - Done when: `research/disc-03-launch-matrix.md` lists 8 providers × 3 browsers × logged
    in/out, and for each records the landing result, fallback and last-tested date.
  - Links: spec.md AC-05; dossier §9
  - Routing: R-local.paid-secret (needs the household's real provider logins)
- [ ] Task: DISC-04 Availability vendor bake-off
  - Done when: a script compares MotN and Watchmode free tiers on 50 titles, reporting coverage,
    deep-link rate, quota usage and terms fit, and D3 is recommended.
  - Links: research.md §Data
  - Routing: R-cloud-default (API keys go in GitHub Secrets)
- [ ] Task: DISC-05 Voice transcription spike
  - Done when: latency and WER are measured for faster-whisper tiny/base/small on the household
    CPU and for in-browser Whisper, using 20 recorded reactions, and a default model is chosen.
  - Links: research.md §Voice
  - Routing: R-local.device-io (microphone, household hardware)
- [ ] Task: DISC-06 Dual-host deploy spike
  - Done when: a hello FastAPI+Postgres image runs from the same GHCR tag on Coolify (compose) and
    on ACA (`azd up`), and the gotchas are appended to research.md §Deployment.
  - Links: architecture.md §Deployment topology
  - Routing: R-local.paid-secret (Coolify server + Azure subscription credentials)

## Milestone 1 — Skeleton & evidence

- [ ] Task: T-SCAFFOLD Scaffold `apps/taste-engine`
  - Done when: FastAPI `/healthz` and an `/v1` OpenAPI endpoint exist; Alembic is set up; the
    React+Vite PWA shell is served by the API; there is a multi-stage Dockerfile and a
    `compose.yaml` (api, worker, migrate, postgres, optional stt); a CI workflow covers lint,
    tests and an image push to GHCR; and `scripts/smoke.sh` checks `/healthz` and `/v1/openapi.json`.
  - Links: architecture.md §Components & interfaces
  - Dependencies: DISC-06
  - Routing: R-cloud-default
- [ ] Task: OPS-01 Coolify deployment
  - Done when: the compose file uses `SERVICE_FQDN_API_8000`, `SERVICE_PASSWORD_*` and
    `${VAR:?}` for required keys; migrate has `restart: "no"`; no host ports are published;
    runbook.md has the Coolify steps; and smoke is green against the Coolify URL.
  - Dependencies: T-SCAFFOLD
  - Routing: R-local.paid-secret (Coolify server access) for the apply step; authoring is cloud
- [ ] Task: OPS-02 Azure deployment
  - Done when: `azure.yaml` and `infra/azure/main.bicep` provision the ACA environment, api and
    worker apps, Postgres Flexible B1ms, Key Vault with managed identity, a capped Log Analytics
    workspace and a migration job; `azd up` deploys the same GHCR tag; and smoke is green.
  - Dependencies: T-SCAFFOLD
  - Routing: R-cloud-default for authoring; R-local.paid-secret for `azd up`
- [ ] Task: CORE-01 Event store & importers
  - Done when: versioned event schemas and migrations exist; Letterboxd, IMDb, Netflix and Trakt
    parsers work with fixtures; there is an unmatched-title review queue; and AC-01 passes.
  - Dependencies: T-SCAFFOLD
  - Routing: R-cloud-default
- [ ] Task: CORE-02 Viewers, auth, export/restore, deletion
  - Done when: `AUTH_MODE=passphrase|oidc` works; viewer isolation is in place; and AC-02 and
    AC-03 pass.
  - Dependencies: CORE-01
  - Routing: R-cloud-default (security-sensitive → `acceptEdits`)

## Milestone 2 — Taste baseline, discover & launch

- [ ] Task: CAT-01 TMDB catalog adapter
  - Done when: the adapter has a cache TTL of at most 6 months, the `/find` IMDb crosswalk and an
    attribution component, and its contract tests use recorded fixtures.
  - Dependencies: CORE-01, DISC-02
  - Routing: R-cloud-default
- [ ] Task: AV-01 Availability adapter & launch chain
  - Done when: the vendor adapter from D3 is in place; `GET /v1/titles/{id}/offers` returns opaque
    URLs following the fallback chain; link-health events are logged; and the AC-05 test passes.
  - Dependencies: CAT-01, DISC-03, DISC-04
  - Routing: R-cloud-default
- [ ] Task: ML-01 Evaluation harness + baselines A/B
  - Done when: there is a temporal-split harness reporting NDCG@10, Recall@20 and coverage;
    Baselines A and B run on household and MovieLens fixtures; and the report is committed.
  - Dependencies: CORE-01, CAT-01
  - Routing: R-cloud-default
- [ ] Task: ML-02 Genome v0 + Personal v1 ranker
  - Done when: a regularized ordinal model and evidence-linked explanations exist; features follow
    the D1 decision; the AC-04 test passes; and the benchmark is compared against ML-01.
  - Dependencies: ML-01
  - Routing: R-cloud-default
- [ ] Task: UX-02 Discover, Title & handoff UI
  - Done when: the Discover feed, "available now" toggle, Title page and *Watch on X* button
    (new tab, `rel="noopener noreferrer"`) are built, and a Playwright e2e covers import →
    discover → launch.
  - Dependencies: AV-01, ML-02
  - Routing: R-cloud.e2e-headless

## Milestone 3 — Feedback & voice

- [ ] Task: UX-01 Reaction UI + push-to-talk
  - Done when: the text box and a MediaRecorder push-to-talk button (with recording indicator and
    cancel) are built, there is a review/accept/edit/undo UI, and e2e uses fake audio.
  - Dependencies: UX-02
  - Routing: R-cloud.e2e-headless
- [ ] Task: ML-03 STT + structured extraction
  - Done when: the STT adapter (faster-whisper container) and the OpenAI-compatible extraction
    with a JSON schema are built; there is a labeled set of 50+ ambiguous or conditional
    reactions; precision and mistaken-generalization rates are reported; and AC-06 passes.
  - Dependencies: CORE-01, DISC-05
  - Routing: R-cloud-default (local model endpoint mocked in CI)
- [ ] Task: PRIV-01 Consent & egress guard
  - Done when: the `CLOUD_AI_CONSENT` flag, consent event and UI indicator are built; an outbound
    host allow-list is in place; and the AC-07 tests pass.
  - Dependencies: ML-03
  - Routing: R-cloud-default (security-sensitive → `acceptEdits`)

## Milestone 4 — Planner

- [ ] Task: PLAN-01 Rotation planner
  - Done when: the planner is built per D4 (our own enumerator or the PenguWatch adapter), uses
    hand-calculated fixtures (overlapping providers, budget, binge-readiness), and AC-09 passes.
  - Dependencies: AV-01, ML-02, DISC-01
  - Routing: R-cloud-default
