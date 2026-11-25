# Plan: taste-engine

Every milestone must end with green CI. Milestones show dependency order, not dates. Each one maps
to a dossier milestone (§10), narrowed to the browser MVP. Task IDs are listed in
[`tasks.md`](./tasks.md).

## Milestone 0 — Discovery & research spikes (in parallel)

**Goal:** turn the desk research in [`research.md`](./research.md) into tested facts. Then decide
D1–D5.

- DISC-01: deploy PenguWatch, Sofa and Findarr at pinned commits on a local or Coolify host.
  Record imports, APIs, UI notes and security posture. Decide D4.
- DISC-02: review licenses and data terms (TMDB §1.C AI clause, MotN, Watchmode, MovieLens).
  Draft the TMDB clarification email. Feeds D1/D2.
- DISC-03: build a provider web-launch matrix covering Netflix, Prime, Disney+, Max, Hulu,
  Apple TV+, Paramount+ and Peacock. Test each in Chrome, Safari and Firefox, logged in and
  logged out, and record the fallback behaviour.
- DISC-04: compare availability vendors using 50 household titles. Measure coverage, deep-link
  hit rate, quota fit and terms. Decide D3.
- DISC-05: run a voice spike. Compare faster-whisper model sizes on the household CPU against
  in-browser Whisper for latency and accuracy, using 20 recorded reactions.
- DISC-06: run a deploy spike. Deploy a hello-world FastAPI plus Postgres compose to Coolify,
  then the same image to ACA via `azd`. Record any gotchas.

**Exit:** every decision D1–D5 is recorded in `research.md`, with evidence links. No product code
is written yet, apart from the spike throwaways in `examples/` or a scratch branch.

## Milestone 1 — Skeleton & evidence (deployable on both hosts)

- T-SCAFFOLD: scaffold `apps/taste-engine` (FastAPI, Alembic, React PWA shell, Dockerfile,
  `compose.yaml`), the CI workflow and the smoke script.
- OPS-01: deploy to Coolify (compose app, env contract, migrations, health check, backups).
- OPS-02: deploy to Azure (`azd` + Bicep, ACA, Postgres Flexible, Key Vault, GHCR pull).
- CORE-01: build the event schemas, migrations, Letterboxd/IMDb/Netflix/Trakt importers and
  idempotency.
- CORE-02: add viewers, auth modes, export/restore and deletion.

**Exit:** AC-01, AC-02, AC-03 and AC-08 pass. The smoke test is green against both hosts.

## Milestone 2 — Taste baseline, discover & launch (first vertical slice)

- CAT-01: add the TMDB catalog adapter, cache, attribution and ID crosswalk.
- AV-01: add the availability adapter for the vendor chosen in D3, plus the launch fallback
  chain and link-health log.
- ML-01: build the evaluation harness (temporal split) with Baseline A and Baseline B.
- ML-02: build the genome v0 and the Personal v1 ranker, with explanations.
- UX-02: build the Discover feed, Title page, "available now" filter and *Watch on X* handoff.

**Exit:** AC-04 and AC-05 pass. The benchmark report is committed, and Personal v1 is compared
against the baselines.

## Milestone 3 — Feedback & voice

- UX-01: add a text reaction box and browser push-to-talk (MediaRecorder), with the
  review/accept/undo UI.
- ML-03: add STT adapter, LLM extraction (schema-constrained), tentative observations and a
  hand-labeled test set.
- PRIV-01: add the consent flag, an egress guard and an audio-discard test.

**Exit:** AC-06 and AC-07 pass. The end-to-end vertical slice demo runs on both hosts.

## Milestone 4 — Rotation planner

- PLAN-01: build the planner, either our own greedy enumerator or the PenguWatch adapter (per D4),
  plus subscription and budget UI.

**Exit:** AC-09 passes.

## Later (post-MVP, not planned in detail)

- Group ("watch together") recommendations.
- Phone pairing via QR code.
- An Android TV / Fire TV handoff spike.
- Hybrid collaborative signals.
- Upstream PRs (external score interface).
