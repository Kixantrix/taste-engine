# Runbook: taste-engine

Status: **draft.** These steps are the target procedure. OPS-01 and OPS-02 finalize them after
the DISC-06 deploy spike.

## Deploy

**Local / plain Docker**

```bash
cp apps/taste-engine/.env.example .env   # set AVAILABILITY_API_KEY, HOUSEHOLD_PASSPHRASE
docker compose -f apps/taste-engine/compose.yaml up -d
SMOKE_BASE_URL=http://localhost:8000 scripts/smoke.sh
```

**Coolify (self-host)**

1. Create a new resource, choose **Docker Compose** from the Git repo, and set Base Directory
   `apps/taste-engine` and compose file `compose.yaml`.
2. Fill in the required variables that Coolify flags (`${VAR:?}`). Coolify generates
   `SERVICE_PASSWORD_*` itself.
3. Set the domain on `api` (the proxy target is port 8000), then deploy. The `migrate` service
   runs once.
4. Enable scheduled Postgres backups to S3-compatible storage.
5. Run `SMOKE_BASE_URL=https://<domain> scripts/smoke.sh`.

**Azure**

```bash
azd auth login
azd env new taste-prod && azd env set IMAGE_TAG <tag>
azd up        # provisions ACA env, api/worker apps, Postgres Flexible, Key Vault, migration job
SMOKE_BASE_URL=$(azd env get-value API_URL) scripts/smoke.sh
```

## Operate

- **Health:** `/healthz` reports liveness. `/readyz` checks the database, the migration version
  and that the STT endpoint is reachable when configured.
- **Jobs:**
  - Catalog refresh runs nightly. It pulls from Wikidata (SPARQL, rate-limited, with a descriptive User-Agent) and TVmaze.
  - Availability refresh runs on demand and nightly for watchlisted titles, within vendor quota.
- **Quotas:** the vendor quota counter is surfaced at `/v1/admin/status`. The app degrades to
  cached offers when the quota is exhausted.
- **Logs:**
  - Coolify: container logs in the UI.
  - Azure: Log Analytics, with a daily ingestion cap.

## Debug

- Import stuck → check the job row in `jobs` and the worker logs. Unmatched titles are listed in
  the review queue, not reported as errors.
- Launch link wrong → check the link-health event for that title and re-run the DISC-03 matrix
  row.
- Voice failing → call `STT_URL/health`. Check the browser mic permission and whether the
  `CLOUD_AI_CONSENT` guard rejected a cloud endpoint.

## Rollback

- Images are immutable GHCR tags. To roll back:
  - Coolify: redeploy the previous tag/commit.
  - Azure: `azd env set IMAGE_TAG <prev> && azd deploy`.
- Migrations must be backward-compatible for one release (expand → contract). Restore from a
  backup only for data corruption.

## Secrets & access

- **Secrets:** `AVAILABILITY_API_KEY`, `HOUSEHOLD_PASSPHRASE` or `OIDC_*`, and
  `DATABASE_URL`.
  - Coolify keeps them in env variables.
  - Azure keeps them in Key Vault, accessed via managed identity.
  - They never live in git or images.
- **Provider credentials** are never stored, by design.
- **Backups** contain viewing history and transcripts, so they must be encrypted at rest.
  Retention is 30 days by default, and deleting a profile is complete once its backups age out.
