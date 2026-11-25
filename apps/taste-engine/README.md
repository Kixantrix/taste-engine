# Taste Engine

FastAPI and a React/Vite shell packaged together as one image. `api` serves the API and PWA;
`worker` is the Postgres-backed queue entrypoint stub; `migrate` upgrades the database before
the application starts.

## Local Compose

Run from the repository root; its Compose defaults match `.env.example`:

```sh
docker compose -f apps/taste-engine/compose.yaml up --build
```

Use the example file (or a local, untracked copy) to override values:

```sh
docker compose --env-file apps/taste-engine/.env.example \
  -f apps/taste-engine/compose.yaml up --build
```

Only the API is published, on port `8000`. Check `http://localhost:8000/`, `/healthz`,
`/readyz`, and `/v1/openapi.json`. The sample database password is only for local development;
replace environment values with deployment secrets for hosted use.

Apply later migrations with `docker compose -f apps/taste-engine/compose.yaml run --rm migrate`.
The migration service is a one-shot container and does not restart automatically.

## Backups

For local development, create a dump outside the repository:

```sh
docker compose -f apps/taste-engine/compose.yaml exec -T postgres \
  pg_dump -U taste_engine taste_engine > "$HOME/taste-engine.sql"
```

Restore into a stopped or disposable local database with:

```sh
cat "$HOME/taste-engine.sql" | docker compose -f apps/taste-engine/compose.yaml \
  exec -T postgres psql -U taste_engine taste_engine
```

For Coolify, configure its scheduled PostgreSQL backups and off-host retention; do not rely on
the Compose data volume as a backup. Azure uses PostgreSQL Flexible Server point-in-time restore.

## Development

```sh
python -m pip install -e 'apps/taste-engine[dev]'
cd apps/taste-engine
pytest tests/unit -q
PGUSER=taste_engine PGPASSWORD=local-dev-password \
  DATABASE_URL='postgresql+psycopg://localhost:5432/taste_engine' \
  pytest tests/integration -q
```

Web checks run from the repository root after installing the workspace dependencies:

```sh
pnpm install
pnpm -C apps/taste-engine/web lint
pnpm -C apps/taste-engine/web typecheck
pnpm -C apps/taste-engine/web test
```

Configuration is read from environment variables only. `DATABASE_URL`, `AUTH_MODE`,
`PUBLIC_BASE_URL`, and `CATALOG_USER_AGENT` are required; cloud AI consent defaults to false
and region defaults to `US`.
