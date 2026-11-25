# Research: taste-engine (browser MVP)

Desk research from 24 Nov 2026. It combines web and doc reading with GitHub metadata. **Nothing
here has been installed or tested hands-on.** Items marked *(unverified)* came from background
knowledge and must be confirmed in the matching M0 spike before we rely on them.
Brief: [`docs/dossier.md`](../../../docs/dossier.md).

## Research questions

| ID | Question | Answered by | Status |
|---|---|---|---|
| RQ-1 | Which existing project, if any, should be the shell? | §Upstream, DISC-01 | Desk answer: thin new shell |
| RQ-2 | Which licensed data source gives US availability and web launch links? | §Data, DISC-04 | Open metadata (Wikidata/TVmaze/Wikipedia) + MotN availability; confirm in DISC-04 |
| RQ-3 | Do provider web links land on the title page? | DISC-03 matrix | Open; needs hands-on testing |
| RQ-4 | How do we deploy the same images to Coolify and Azure? | §Deployment, OPS-01/02 | Desk answer below |
| RQ-5 | How do we capture voice privately in a browser? | §Voice, UX-01 spike | Desk answer below |
| RQ-6 | Which history exports are realistically available, and how good is their signal? | §Import, CORE-01 | Desk answer below |
| RQ-7 | Can a personal ranker beat simple baselines on household data? | ML-01/ML-02 | Open; needs data |
| RQ-8 | Do TMDB terms allow an ML ranker built on TMDB data? | DISC-02, D1 | **Decided 2026-11-24 (D1): no TMDB** |

## Upstream (RQ-1)

| Repo | License | Stack | Activity | Relevance |
|---|---|---|---|---|
| [PenguWatch](https://github.com/pengupowered/penguwatch) | MIT | Python | Active, young, 1★ | Subscription/rotation planner. REST API, webhooks and importable custom rating sources make it the best integration target. Its default compose exposes `0.0.0.0:8080` without auth. |
| [Sofa](https://github.com/jakejarvis/sofa) | MIT | TS/Bun | Very active, 48★ | Strong import pipeline (Trakt, Simkl, Letterboxd, Plex/Jellyfin webhooks), OIDC and TMDB availability. Public API is unverified. |
| [Findarr](https://github.com/Lillifee/findarr) | MIT | TS | Active, 64★ | Closest concept (learns taste from ratings). Extension points are unverified. Useful as a UX reference. |
| [Streamline](https://github.com/abhichandra21/streamline) | MIT | Python | Weeks old, 1★ | History→TMDB matching patterns. Its ranking is LLM-driven. |
| [MediaShelf](https://github.com/ghltshubh/mediashelf) | AGPL-3.0 | Python | Active | Streaming index and router. Copyleft, so we would only integrate through its API, never embed it. |
| [MultiStream](https://github.com/renaudallard/multistream) | **No license** | Kotlin/Android | 2026-06 | Can't reuse it. Its provider-capability pattern is still worth borrowing as an idea. |
| [Yamtrack](https://github.com/FuzzyGrim/Yamtrack) | AGPL-3.0 | Python/Django | Very active, 3.9k★ | Mature tracker. AGPL limits embedding it. |
| [recommenders](https://github.com/recommenders-team/recommenders) | MIT | Python lib | Active | Offline algorithms and evaluation. Use as a library. |
| [RecAI](https://github.com/microsoft/RecAI) | MIT | Research | Quiet | Source of ideas only. |

**Desk recommendation:** build a **thin new shell** with its own event store, importers and score
API. The taste/ranking core is the product, and no candidate offers a pluggable ranker. After
that, integrate **PenguWatch first**, pushing our scores in as a custom rating source and
possibly reusing its planner instead of writing PLAN-01. Integrate **Sofa second** as a source of
history. DISC-01 must confirm all of this at pinned commits.

## Data (RQ-2, RQ-8)

- **TMDB**
  - Metadata, images and ID crosswalk (`/find` by IMDb ID).
  - Free for non-commercial use with attribution. Caching is capped at 6 months.
  - [Terms](https://www.themoviedb.org/api-terms-of-use) §1.C forbids using TMDB content "in connection with… a machine learning or AI based Application". **This conflicts directly with a taste engine that ranks on TMDB-derived features.** → Decision D1.
  - `watch/providers` comes from JustWatch and requires JustWatch attribution. It lists providers only and has **no deep links**, just a TMDB `/watch` landing page.
- **Streaming Availability API (Movie of the Night)** ([docs](https://docs.movieofthenight.com/))
  - Deep links per movie, show, season and episode, plus expiry dates and prices, across 65 countries.
  - The free tier allows 100 requests/day, so we must cache lookups per title on demand.
  - We have not read the terms yet.
- **Watchmode** ([pricing](https://api.watchmode.com/pricing))
  - The free tier gives 2,500 credits/month, is non-commercial, and requires a refresh within 30 days.
  - App/episode deep links appear to be Startup tier and above ($349/mo).
  - It is our backup source.
- **JustWatch:** no public API. Don't scrape it.
- **Trakt / Simkl:** history and ID crosswalk via OAuth. No deep links *(unverified)*. Trakt metadata is TMDB-sourced, so we use its IDs only.
- **Wikidata** (e.g. Netflix ID P1874): only for patchy ID backfill.
- **Launch-link policy**
  - Treat provider URLs as **opaque values supplied by the availability API**, never as patterns we construct ourselves.
  - Fallback chain: deep link → provider search URL → provider home page.
  - Log broken links with a last-tested date.

**MVP data stack (D1 decided: fully open, no TMDB):**
- **Wikidata (CC0)** provides entities, IDs and structured features.
- **TVmaze (CC BY-SA)** provides TV seasons and episodes.
- **Wikipedia (CC BY-SA)** provides overviews and the text used to derive genome attributes.
- **MotN** provides availability and deep links.
- Our own attribute "genome" comes only from these sources plus user evidence.

Options considered for D1:
- (a) Ask TMDB for clarification.
- (b) Hybrid, using TMDB for display only.
- (c) Use a commercial vendor.
- **Chosen: fully open.** Tradeoff: poster imagery and overviews are weaker, and very new or obscure titles have thinner coverage.
- Imagery uses availability-vendor images only where their terms allow. Otherwise it falls back to text cards.

### Open metadata sources (replacing TMDB)

| Source | License / terms | Coverage | Use for |
|---|---|---|---|
| [Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing) | **CC0** structured data. Any use, no attribution needed. | Films and series. Genres, cast/crew, country, year, awards, based-on, IMDb/TMDB/Netflix IDs | Core ID crosswalk and structured features. Safest ML base. |
| Wikipedia plot/reception text | CC BY-SA 4.0. Attribute it; derived numeric features are very likely fine *(confirm)*. | Most notable titles | LLM-derived genome attributes (tone, pacing, themes). |
| [TVmaze API](https://www.tvmaze.com/api) | **CC BY-SA 4.0** data. Any use with credit and link. | TV only. Strong episode/season/schedule data and US network/web-channel info. | TV structure, episode cadence, season-readiness for the planner. |
| IMDb non-commercial datasets | Personal and non-commercial use only. No redistribution. *(ML terms unverified)* | Very broad. Ratings and vote counts, basic genres. | Popularity and quality priors (Baseline A), if the terms allow. |
| MovieLens 32M / Tag Genome | Research, non-commercial, no redistribution without permission | Movies, ≤2023 | Offline evaluation and attribute-vocabulary research only. Don't ship it. |
| Availability vendor payloads (MotN / Watchmode) | Per vendor contract *(check ML/cache clauses in DISC-02)* | Titles they track | Genres, overview and ratings bundled with availability. |
| User evidence | Ours | Household | Strongest personal signal (reactions, ratings, imports). |
| Commercial vendors (Gracenote, TheTVDB licensed) | Paid | Comprehensive | Only if D2 changes to commercial. |

**Design rule:**
- Every catalog field and genome feature records its source and license.
- Swapping a source must not require re-collecting user evidence.
- Wikimedia API etiquette applies: a descriptive User-Agent, rate limits, and bulk work against dumps rather than live SPARQL.

## Import (RQ-6)

- **Netflix**
  - Per-profile "Viewing activity" CSV: Title and Date only, no ratings. Episode rows look like `Show: Season N: Episode`.
  - Full account data export: `ViewingActivity.csv` with profile, start time, duration and device. It can take up to 30 days.
  - Low signal. Titles need fuzzy matching against Wikidata/TVmaze labels, using the Netflix ID (P1874) where available.
- **Letterboxd** ZIP: `watched.csv`, `ratings.csv` and `diary.csv` *(unverified columns)*. A strong signal for movies.
- **IMDb** ratings CSV: `Const` (IMDb ID), `Your Rating` and `Date Rated` *(unverified)*. Maps exactly via Wikidata IMDb ID (P345).
- **Trakt:** OAuth API or export. Best for TV.
- **Parsing:** parse on the household server (or in the browser), then discard the raw file once events are written.

## Deployment (RQ-4)

**Coolify** ([compose docs](https://coolify.io/docs/applications/builds/docker-compose))
- A Git-backed "Docker Compose" application supports webhooks, branch deploys and PR previews.
- Magic variables:
  - `SERVICE_FQDN_<SVC>_<PORT>` routes a domain to a container port.
  - `SERVICE_PASSWORD_<ID>` generates a secret. The ID must have no underscore.
- `${VAR:?}` marks a variable as required.
- Paths resolve from the Base Directory.
- Set `restart: "no"` on one-shot migration containers.
- Traefik and Let's Encrypt are built in. Scheduled tasks and S3 backups are available *(verify on our version)*.

**Azure**
- **Container Apps (ACA)** runs the same OCI images and scales to zero. ACA Jobs handle cron and queue work, and its free grant covers idle households ([pricing](https://azure.microsoft.com/en-us/pricing/details/container-apps/)).
- `az containerapp compose create` exists but is limited ([docs](https://learn.microsoft.com/en-us/cli/azure/containerapp/compose)). Use **`azd` + Bicep** as the Azure source of truth.
- **PostgreSQL Flexible Server** B1ms costs about $12/mo compute.
- **Key Vault** with managed identity holds secrets.
- **Blob storage** is not S3-compatible, so it goes behind an adapter.
- **Easy Auth** (Entra) is optional as an outer layer only.

**Portability decisions** (proposed in `architecture.md`)
- One compose file is the source of truth for local dev and Coolify. A separate Bicep/`azd` stack for Azure uses the same GHCR images.
- **Postgres on every hosted target.** SQLite is for dev/tests only, and must never sit on Azure Files/SMB because locking breaks there.
- In-app OIDC via Authlib: Pocket ID/Authentik on Coolify, Entra on Azure, plus a "household passphrase" mode for the simplest installs.
- Object storage behind an S3/Blob adapter. It is optional for the MVP, because raw audio isn't retained.
- A Postgres-backed job queue (e.g. `procrastinate` / `SKIP LOCKED`). It runs as a worker container on Coolify and as an ACA Job/app on Azure.

## Voice (RQ-5)

- The **Web Speech API sends audio to the browser vendor's cloud** on Chrome and Edge ([MDN](https://developer.mozilla.org/docs/Web/API/SpeechRecognition)). Firefox doesn't support it. A newer `processLocally` flag exists but depends on downloaded language packs. So Web Speech must not be the default.
- **Default:** capture with `MediaRecorder` and transcribe with a self-hosted **faster-whisper** container. Discard the audio after transcription.
- Optional modes:
  - In-browser Whisper (transformers.js/WebGPU), which needs a large model download.
  - Cloud STT, via Azure AI Speech or Web Speech, only behind explicit consent.
- LLM extraction goes through an OpenAI-compatible adapter (`LLM_BASE_URL`): Ollama/llama.cpp locally, or Azure OpenAI with consent. The Azure data-handling terms are not yet verified.

## Open decisions

| ID | Decision | Recommendation | Who |
|---|---|---|---|
| D1 | How do we handle the TMDB ML/AI clause? | **Decided 2026-11-24:** drop TMDB. Use Wikidata, TVmaze and Wikipedia for all metadata. | Human ✅ |
| D2 | Will this ever be commercial or multi-household hosted? | No for the MVP. This keeps the Watchmode and MotN free tiers viable. | Human |
| D3 | Availability vendor | MotN free tier first, Watchmode as backup. Confirm in DISC-04. | DISC-04 |
| D4 | Shell | Thin new shell, with PenguWatch integration as the first adapter. | DISC-01 |
| D5 | Azure role | Managed reference deployment. Coolify is the self-host target. | Human (confirm) |
| D6 | Frontend stack | React + Vite + TS PWA served by the API container, which matches `apps/kerrigan-dashboard` tooling. | Proposed |
