# Tasks: taste-engine

Each task ends with green CI and has explicit "done" criteria. The Routing column cites
[`delegation-rubric`](../../../.github/skills/delegation-rubric/SKILL.md).

## Milestone 0 — Discovery

GitHub issue numbers are shown as `#N`. Tasks marked *(new)* get an issue at dispatch time.

- [ ] Task: DISC-01 Upstream shell audit (PenguWatch, Sofa, Findarr) — #1
  - Done when: `research/disc-01-upstream.md` records the pinned commit, deploy commands, import
    results, API surface (whether it can accept external scores), auth/security posture, and a
    D4 recommendation.
  - Links: research.md §Upstream; dossier §3
  - Routing: R-local.human-judgment (hands-on UX evaluation with household data)
- [ ] Task: DISC-02 License & data-terms review — #2
  - Done when: `research/disc-02-licenses.md` contains an SPDX table for the candidates; the
    MotN, Watchmode, IMDb-dataset and MovieLens terms (caching, ML use, imagery) are summarized with
    the clauses quoted; the open-data attribution requirements are listed; and D2/D3 inputs are
    written up.
  - Links: research.md §Data, D1, D2
  - Routing: R-cloud-default
- [ ] Task: DISC-03 Provider web-launch matrix — #3
  - Done when: `research/disc-03-launch-matrix.md` lists 8 providers × 3 browsers × logged
    in/out, and for each records the landing result, fallback and last-tested date.
  - Links: spec.md AC-05; dossier §9
  - Routing: R-local.paid-secret (needs the household's real provider logins)
- [ ] Task: DISC-04 Availability vendor bake-off — #4
  - Done when: a script compares MotN and Watchmode free tiers on 50 titles, reporting coverage,
    deep-link rate, quota usage and terms fit, and D3 is recommended.
  - Links: research.md §Data
  - Dependencies: external:MOTN_API_KEY / WATCHMODE_API_KEY in the repo `copilot` environment
  - Routing: R-cloud-default (API keys go in GitHub Secrets)
- [ ] Task: DISC-05 Maintainer discussions on external score interfaces — #5
  - Done when: PenguWatch and Sofa maintainers have been contacted via public discussions, and
    their responses are recorded.
  - Dependencies: DISC-01
  - Routing: R-local.human-judgment (speaks for the project)
- [ ] Task: DISC-06 Voice transcription spike *(new)*
  - Done when: latency and WER are measured for faster-whisper tiny/base/small on the household
    CPU and for in-browser Whisper, using 20 recorded reactions, and a default model is chosen.
  - Links: research.md §Voice
  - Routing: R-local.device-io (microphone, household hardware)

## Milestone 1 — Skeleton & evidence

- [ ] Task: OPS-01 Scaffold `apps/taste-engine` + compose + CI + smoke — #14
  - Done when:
    - FastAPI serves `/healthz` and an `/v1` OpenAPI endpoint, with Alembic set up.
    - The React+Vite PWA shell is served by the API.
    - There is a multi-stage Dockerfile and a `compose.yaml` (api, worker, migrate, postgres).
    - A CI workflow covers lint, tests, a compose smoke run and an image push to GHCR.
    - `scripts/smoke.sh` gains an opt-in taste-engine section (`TASTE_SMOKE_BASE_URL`).
  - Links: architecture.md §Components & interfaces, §Deployment topology
  - Briefing: `.specify/briefings/taste-OPS-01.md`
  - Routing: R-cloud-default
- [ ] Task: OPS-02 Coolify deployment *(new)*
  - Done when:
    - The compose file uses `SERVICE_FQDN_API_8000`, `SERVICE_PASSWORD_*` and `${VAR:?}` for
      required keys, and migrate has `restart: "no"`.
    - No host ports are published.
    - runbook.md has the Coolify steps, and smoke is green against the Coolify URL.
  - Dependencies: OPS-01
  - Routing: R-cloud-default for authoring; R-local.paid-secret (Coolify server access) for apply
- [ ] Task: OPS-03 Azure deployment *(new)*
  - Done when:
    - `azure.yaml` and `infra/azure/main.bicep` provision:
      - the ACA environment, with api and worker apps;
      - Postgres Flexible B1ms;
      - Key Vault with managed identity;
      - a capped Log Analytics workspace;
      - a migration job.
    - `azd up` deploys the same GHCR tag, and smoke is green.
  - Dependencies: OPS-01
  - Routing: R-cloud-default for authoring; R-local.paid-secret for `azd up`
- [ ] Task: CORE-01 Event store & importers — #6
  - Done when: versioned event schemas and migrations exist; Letterboxd, IMDb, Netflix and Trakt
    parsers work with fixtures; there is an unmatched-title review queue; and AC-01 passes.
  - Dependencies: OPS-01
  - Routing: R-cloud-default
- [ ] Task: CORE-02 Viewers, auth, export/restore, deletion — #7
  - Done when: `AUTH_MODE=passphrase|oidc` works; viewer isolation is in place; and AC-02 and
    AC-03 pass.
  - Dependencies: CORE-01
  - Routing: R-cloud-default (security-sensitive → `acceptEdits`)

## Milestone 2 — Taste baseline, discover & launch

- [ ] Task: CAT-01 Open catalog adapter
  - Done when: the Wikidata SPARQL adapter (films/series, IDs, genres, cast) is built; TVmaze
    provides seasons and episodes; Wikipedia provides overview extracts; every field stores
    source and license; there is an attribution footer; title matching resolves ≥90% of the
    household fixture imports; and contract tests use recorded fixtures.
  - Dependencies: CORE-01, DISC-02
  - Routing: R-cloud-default
- [ ] Task: AV-01 Availability adapter & launch chain
  - Done when: the vendor adapter from D3 is in place; `GET /v1/titles/{id}/offers` returns opaque
    URLs following the fallback chain; link-health events are logged; and the AC-05 test passes.
  - Dependencies: CAT-01, DISC-03, DISC-04
  - Routing: R-cloud-default
- [ ] Task: ML-01 Evaluation harness + baselines A/B — #8
  - Done when: there is a temporal-split harness reporting NDCG@10, Recall@20 and coverage;
    Baselines A and B run on household and MovieLens fixtures; and the report is committed.
  - Dependencies: CORE-01, CAT-01
  - Routing: R-cloud-default
- [ ] Task: ML-02 Genome v0 + Personal v1 ranker — #9
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

- [ ] Task: UX-01 Reaction UI + push-to-talk — #10
  - Done when: the text box and a MediaRecorder push-to-talk button (with recording indicator and
    cancel) are built, there is a review/accept/edit/undo UI, and e2e uses fake audio.
  - Dependencies: UX-02
  - Routing: R-cloud.e2e-headless
- [ ] Task: ML-03 STT + structured extraction — #11
  - Done when: the STT adapter (faster-whisper container) and the OpenAI-compatible extraction
    with a JSON schema are built; there is a labeled set of 50+ ambiguous or conditional
    reactions; precision and mistaken-generalization rates are reported; and AC-06 passes.
  - Dependencies: CORE-01, DISC-06
  - Routing: R-cloud-default (local model endpoint mocked in CI)
- [ ] Task: PRIV-01 Consent & egress guard
  - Done when: the `CLOUD_AI_CONSENT` flag, consent event and UI indicator are built; an outbound
    host allow-list is in place; and the AC-07 tests pass.
  - Dependencies: ML-03
  - Routing: R-cloud-default (security-sensitive → `acceptEdits`)

## Milestone 4 — Planner

- [ ] Task: PLAN-01 Rotation planner — #12
  - Done when: the planner is built per D4 (our own enumerator or the PenguWatch adapter), uses
    hand-calculated fixtures (overlapping providers, budget, binge-readiness), and AC-09 passes.
  - Dependencies: AV-01, ML-02, DISC-01
  - Routing: R-cloud-default

## Superseded

- INT-01 (#13), "single upstream-compatible client adapter": folded into PLAN-01 (PenguWatch
  adapter, per D4) and DISC-01. Close #13 once D4 is decided.
