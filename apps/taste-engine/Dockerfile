FROM node:22-alpine AS web-build
WORKDIR /workspace
RUN corepack enable && corepack prepare pnpm@9.12.2 --activate
COPY pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/kerrigan-dashboard/package.json apps/kerrigan-dashboard/package.json
COPY apps/taste-engine/web/package.json apps/taste-engine/web/package.json
RUN pnpm install --frozen-lockfile --filter taste-engine-web
COPY apps/taste-engine/web apps/taste-engine/web
RUN pnpm --filter taste-engine-web build

FROM python:3.12-slim AS python-build
WORKDIR /build
COPY apps/taste-engine/pyproject.toml .
COPY apps/taste-engine/src src
RUN pip install --no-cache-dir .

FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
RUN groupadd --system taste && useradd --system --gid taste --home-dir /app taste
COPY --from=python-build /usr/local /usr/local
COPY --chown=taste:taste apps/taste-engine/alembic alembic
COPY --chown=taste:taste apps/taste-engine/alembic.ini .
COPY --from=web-build --chown=taste:taste /workspace/apps/taste-engine/web/dist web/dist
USER taste
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=2)" || exit 1
CMD ["uvicorn", "taste_engine.app:app", "--host", "0.0.0.0", "--port", "8000"]
