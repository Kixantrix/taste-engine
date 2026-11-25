from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from alembic.config import Config
from alembic.script import ScriptDirectory
from taste_engine.settings import Settings, get_settings

SOURCE_APP_DIR = Path(__file__).resolve().parents[2]
APP_DIR = Path.cwd() if (Path.cwd() / "alembic").is_dir() else SOURCE_APP_DIR
WEB_DIR = APP_DIR / "web"
DIST_DIR = WEB_DIR / "dist"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.settings = get_settings()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="Taste Engine",
        version="0.1.0",
        openapi_url="/v1/openapi.json",
        lifespan=lifespan,
    )

    @app.get("/healthz")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/readyz")
    def readiness(request: Request) -> JSONResponse:
        settings: Settings = request.app.state.settings
        config = Config(str(APP_DIR / "alembic.ini"))
        config.set_main_option("script_location", str(APP_DIR / "alembic"))
        config.set_main_option("sqlalchemy.url", settings.database_url.replace("%", "%%"))
        head = ScriptDirectory.from_config(config).get_current_head()
        if head is None:
            return JSONResponse({"status": "not_ready"}, status_code=503)

        engine = create_engine(
            settings.database_url,
            pool_pre_ping=True,
            connect_args={"connect_timeout": 2},
        )
        try:
            with engine.connect() as connection:
                revisions = connection.execute(
                    text("SELECT version_num FROM alembic_version")
                ).scalars().all()
            if revisions == [head]:
                return JSONResponse({"status": "ok"})
        except SQLAlchemyError:
            pass
        finally:
            engine.dispose()
        return JSONResponse({"status": "not_ready"}, status_code=503)

    @app.get("/", include_in_schema=False)
    def index() -> FileResponse:
        built_index = DIST_DIR / "index.html"
        index_file = built_index if built_index.is_file() else WEB_DIR / "index.html"
        return FileResponse(index_file)

    assets_dir = DIST_DIR / "assets"
    if assets_dir.is_dir():
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    return app


app = create_app()
