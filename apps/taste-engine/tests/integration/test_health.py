from fastapi.testclient import TestClient

from taste_engine.app import app


def test_healthz_is_independent_of_database() -> None:
    with TestClient(app) as client:
        response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz_requires_reachable_database_at_migration_head() -> None:
    with TestClient(app) as client:
        response = client.get("/readyz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
