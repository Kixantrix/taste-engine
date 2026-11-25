# Briefing: taste-DISC-02 (issue #2)

## Objective
Produce a cited license and data-terms review that unblocks decisions D2 (commercial
posture) and D3 (availability vendor) for taste-engine. The task is research only; no code.

## Context
- `specs/projects/taste-engine/research.md`, sections §Upstream, §Data and §Open decisions.
- D1 has already been decided: **no TMDB**. Metadata comes from Wikidata, TVmaze and Wikipedia.
  Do not reopen D1.

## Acceptance criteria
- AC-DISC02-a: `specs/projects/taste-engine/research/disc-02-licenses.md` contains an SPDX table
  for PenguWatch, Sofa, Findarr, Streamline, MediaShelf, MultiStream, Yamtrack and `recommenders`.
  Each row records the commit SHA inspected, the LICENSE path and any NOTICE, CLA or contribution
  obligations. — level: scenario — environment: manual-human — test: human review of the doc
  (checklist at the bottom of the doc)
- AC-DISC02-b: The doc has a terms table for Streaming Availability API (Movie of the Night),
  Watchmode, TVmaze, Wikidata, Wikipedia (CC BY-SA text), the IMDb non-commercial datasets and
  MovieLens 32M / Tag Genome.
  - Each row covers caching/retention, ML/AI use, attribution, imagery rights, commercial
    restrictions and redistribution.
  - Each claim is backed by a **quoted clause and URL**, with the retrieval date.
  - Anything not found is marked "not stated", never guessed.
  - level: scenario — environment: manual-human — test: same review checklist
- AC-DISC02-c: A "Decision inputs" section states:
  - which availability vendors stay viable for a **non-commercial household** deployment and
    which for a **commercial** one (D2/D3 matrix);
  - the exact attribution strings and UI placements we must implement.
  - level: scenario — environment: manual-human — test: same review checklist
- AC-DISC02-d: `research.md` §Data has a one-paragraph summary linking to the new doc. Items
  previously marked *(unverified)* are updated to verified or contradicted. — level: unit —
  environment: cloud-linux — test: `python -m tools.validators.check_artifacts` passes

## Scope
- Touch: `specs/projects/taste-engine/research/disc-02-licenses.md` (new), and
  `specs/projects/taste-engine/research.md` (§Data and §Upstream summary lines only).
- Read-only: everything else.
- Out of scope:
  - Making the D2/D3 decisions; present the inputs only.
  - Contacting maintainers (that is DISC-05).
  - Writing code.
  - Reconsidering TMDB.

## Prior decisions
- D1 is decided as fully open metadata with no TMDB (research.md §Open decisions).
- The MVP is a single-household, non-commercial deployment (spec.md §Scope; D2 recommendation).

## Relevant skills (preload)
- block-report: if a vendor's terms are only available after sign-up, emit a block rather than
  guessing.

## Test commands
- unit: `python -m tools.validators.check_artifacts`
- integration: n/a
- smoke: `bash scripts/smoke.sh`

## Routing rule matched
R-cloud-default: public web research and markdown output, with no secrets or devices.

## Budget
- max_turns: 30
- max_premium_requests: 15
