# taste-engine

A local-first, portable **taste engine** for a household's film and TV viewing.

It learns what each viewer enjoys (including spoken, nuanced reactions), ranks titles across the whole catalog independently of which services you currently pay for, and proposes when to activate or pause subscriptions. Playback is always handed off to the legitimate provider's app or website — this project never streams, proxies, or circumvents DRM.

> **Status:** M0 discovery. Nothing is built yet. The full brief lives in [`docs/dossier.md`](docs/dossier.md).

## Principles

- **You own your profile:** exportable history, feedback, inferred preferences and settings.
- **Local-first, not local-only:** local storage and inference by default; cloud model services are explicit opt-in.
- **Taste before availability:** predict enjoyment for any title, then filter to what's playable now.
- **Voice is a primary input:** push-to-talk reactions, never an always-on microphone.
- **Upstream-first:** integrate with and contribute to existing projects (Streamline, Sofa, PenguWatch, MultiStream, …) before forking or rebuilding.
- **Prove it:** every model must beat simple baselines on a reproducible benchmark.

## Non-goals

Streaming server, DRM circumvention, automatic purchases or cancellations, always-on microphone, universal provider authentication, training a foundation model, or a commercial multi-tenant service at launch.

## Roadmap

| Milestone | Deliverable |
|---|---|
| M0 discovery | Upstream repo audit, license review, availability-data and device-handoff spikes → fork-or-integrate decision |
| M1 evidence | Importers, canonical IDs, portable append-only event store, viewer isolation |
| M2 taste baseline | Content genome, embeddings, ranking, explainable recommendations |
| M3 voice | Push-to-talk, local transcription, evidence extraction, undo |
| M4 rotation | Availability adapter, manual subscriptions, viewing/subscription planner |
| M5 living room | TV integration or native client, QR pairing |
| M6 ecosystem | Documented API/SDK, upstream PRs, packaging |

Work is tracked as [GitHub issues](../../issues); see the dossier §10 for the initial backlog.

## How this repo is developed

This repository is built with the [Kerrigan](https://github.com/Kixantrix/kerrigan) agent harness on top of [GitHub Spec Kit](https://github.com/github/spec-kit). Agents start at [`AGENTS.md`](AGENTS.md). Harness files (`.github/agents`, `.github/skills`, `tools/`, `playbooks/`, `specs/kerrigan*`) are upstream Kerrigan and are refreshed with `tools/upgrade-kerrigan.ps1`.

## License

[Apache-2.0](LICENSE). Third-party code, models and data (catalog metadata, MovieLens, provider availability) carry their own terms and are reviewed separately before use.
