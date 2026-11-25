# Spec: taste-engine

> Source brief: [`docs/dossier.md`](../../../docs/dossier.md). Research findings:
> [`research.md`](./research.md). This spec narrows the dossier to the **browser MVP**.

## Goal

Ship a browser-first MVP of a portable, household taste engine: a viewer imports or records
what they have watched, gets a taste-ranked list of films/series, launches a chosen title on
the **provider's official website** (handoff, never playback), reacts in text or by
push-to-talk voice, and sees the next recommendation change with a traceable explanation.

The same container images deploy to **Coolify** (self-hosted, primary portability target) and
**Azure** (managed hosting), with no code forks between the two.

## Scope

MVP (browser, single household, US availability):

- Household with separate viewer identities; simple authentication that works on both hosts.
- History import: Letterboxd CSV, IMDb ratings CSV, Netflix `ViewingActivity.csv`, Trakt
  export (JSON); manual "watched / rate" actions. Idempotent re-import.
- Catalog: TMDB metadata adapter with local cache and required attribution.
- Availability: one authorized availability source (see `research.md` §Data) resolving
  providers and web launch URLs; graceful fallback to provider search / TMDB watch page.
- Append-only, versioned evidence event store (viewing, feedback, corrections) with JSON
  export, restore and genuine deletion.
- Taste baseline: popularity/genre baseline + embedding similarity baseline + first
  regularized personal ranker; explanations grounded in stored evidence.
- Feedback: text box and browser push-to-talk (MediaRecorder → self-hosted
  transcription); structured extraction into tentative observations with review/undo.
- Discover feed (taste-ranked, availability-independent) with an "available now on my
  services" filter; manual subscription state.
- Basic monthly rotation suggestion (enumerated service combinations + greedy schedule).
- Deployment: Docker Compose stack deployable on Coolify; Azure deployment (Container Apps)
  from the same images via `azd`/Bicep.

## Non-goals

- Stream playback, DRM circumvention, provider password collection, scraping providers.
- Automatic subscribe/cancel or any billing action.
- Always-on microphone; cloud upload of audio/transcripts without explicit opt-in consent.
- Native TV / mobile apps (Android TV, Fire TV, iOS) — post-MVP; handoff spike only.
- Episode-level progress sync with providers.
- Multi-tenant commercial SaaS, foundation-model training or LLM fine-tuning.
- Group ("watch together") recommendations beyond a simple per-viewer filter (post-MVP).

## Users & scenarios

- **Viewer** imports Letterboxd + Netflix history, sees a ranked Discover feed, filters to
  "available now", clicks *Watch on Netflix* and lands on the title page in a new tab.
- **Viewer** returns, presses the mic, says "loved the world-building, hated the contrived
  drama", reviews the extracted observations, accepts them, and sees the feed re-rank with
  "because you liked political world-building in X".
- **Viewer** corrects an inference ("no, I don't dislike all flawed characters") and the
  profile rebuilds.
- **Household admin** sets current subscriptions and a monthly budget and gets an
  active / next / wait proposal with reasons.
- **Self-hoster** deploys the stack to Coolify from the repo's compose file; **maintainer**
  deploys the same images to Azure with `azd up`.

## Constraints

- Hard product boundaries from `AGENTS.md` / dossier §2 are non-negotiable.
- Local-first: all user data stays in the household's deployment; cloud AI (e.g. Azure
  OpenAI / Azure AI Speech) is an opt-in adapter, off by default, behind explicit consent.
- Portability: OCI images + 12-factor env config; no host-specific SDKs in the core; storage
  and auth behind adapters.
- Data licensing: respect TMDB / availability-vendor terms (attribution, caching windows,
  non-commercial limits). No unlicensed scraping.
- Upstream-first: prefer integrating/contributing to existing projects where it fits (see
  `research.md` §Upstream).

## Acceptance criteria

Detailed, test-mapped criteria live in [`acceptance-tests.md`](./acceptance-tests.md).
Summary of the first vertical slice (M2 exit):

- AC-01 Importing the same Letterboxd/IMDb/Netflix/Trakt file twice yields identical events.
- AC-02 Profile export → wipe → restore round-trips byte-equivalent canonical JSON.
- AC-03 Deleting a viewer removes their events and derived features.
- AC-04 Discover feed ranks unseen titles for a viewer and each item has ≥1 evidence-backed
  explanation.
- AC-05 "Watch on <provider>" opens the provider's official web URL (or documented
  fallback) in a new tab; no credentials requested by our app.
- AC-06 Text or voice feedback produces tentative observations the viewer can accept,
  edit or undo; accepting changes the next ranking.
- AC-07 Raw audio is discarded after transcription by default; no audio/transcript leaves
  the deployment unless the cloud-AI consent flag is set.
- AC-08 The same image tags deploy and pass the smoke test on Coolify and on Azure.
- AC-09 Rotation planner never double-counts a title across providers and respects budget.

## Risks & mitigations

| Risk | Mitigation |
|---|---|
| Availability data cost/terms | Vendor comparison spike (DISC-04) before committing; adapter interface; cache per contract. |
| Provider web links unstable | Link-compatibility matrix with last-tested dates; fallback chain. |
| SQLite on network file shares (Azure Files/SMB) | Postgres on every hosted target; SQLite only for dev/tests. See `architecture.md`. |
| TMDB terms restrict ML/AI use of TMDB content | Decision D1 in `research.md`; keep ranking features separable from TMDB fields; seek written clarification. |
| Browser speech APIs leak audio to vendor clouds | Do not use Web Speech API by default; MediaRecorder → self-hosted faster-whisper. |
| Taste model adds no value over baselines | Baselines A/B shipped first; benchmark gates (dossier §5.5). |
| Upstream projects unsuitable/unmaintained | M0 audit decides shell vs thin new app; adapters keep us decoupled. |
| Scope creep into TV/native | TV is explicitly post-MVP; only a handoff feasibility spike. |

## Success metrics

- Vertical slice demo: import → discover → launch → react → re-rank with explanation, on
  both Coolify and Azure.
- Personal ranker beats popularity and embedding baselines on NDCG@10 on a temporal split of
  the household's own data (numeric target set after baseline collection).
- ≥80% of tested US provider launch links land on the title page (not just home) on desktop
  browsers, recorded in the compatibility matrix.
- Voice reaction to accepted observation in < 10 s p50 on the household's hardware.
- Zero data egress outside the deployment with default settings (verified by test).
