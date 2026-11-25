# Cost plan: taste-engine

## Cost drivers

- Compute for the api/worker containers.
- Optional STT CPU.
- Managed Postgres (Azure).
- Availability vendor tier.
- Log ingestion (Azure).
- Optional cloud AI calls (Azure OpenAI/Speech, opt-in only).

## Baseline estimate

All figures are desk estimates from Nov 2026 and still need verification.

| Item | Coolify (self-host) | Azure |
|---|---|---|
| App compute | Existing server ($0 marginal) | ACA, within the monthly free grant for one household: ~$0–5 |
| Database | Postgres container: $0 | Postgres Flexible B1ms + 32 GB: ~$15–20 |
| Registry | GHCR: $0 | GHCR: $0 (ACR Basic ~$5 if preferred) |
| Logs / Key Vault / DNS | $0 | ~$2–5 (with Log Analytics capped) |
| STT | Household CPU: $0 | Opt-in Azure AI Speech, usage-based (small); or self-host |
| Data APIs | Wikidata/TVmaze/Wikipedia free; MotN free (100 req/day); Watchmode free (2,500/mo) | Same |
| **Total** | **≈ $0 marginal** | **≈ $20–30 / month** |

Paid availability tiers (Watchmode Startup at $349/mo) are **out of budget** for the MVP. Needing
one would trigger decision D2/D3.

## Guardrails (budgets/alerts/tags)

- Azure:
  - Set a subscription budget of $40/mo, with alerts at 50%, 80% and 100%.
  - Tag all resources `project=taste-engine`.
  - Cap Log Analytics at 0.5 GB/day.
  - Set ACA max replicas to 2.
- Vendor quotas:
  - Use an in-app counter that refuses calls beyond 90% of the daily or monthly quota and serves
    cached data instead.
- Cloud AI:
  - Off by default (`CLOUD_AI_CONSENT=false`).
  - When enabled, apply a monthly token cap in config.

## Scale assumptions

- 1 household, 2–5 viewers, fewer than 10 concurrent requests.
- A catalog cache of about 20–50k titles. Postgres stays under 2 GB.
- Multi-household or commercial use is **not** assumed. That would change data licensing (paid
  availability-vendor tiers) before it changes infrastructure.
