from fastapi.testclient import TestClient

from taste_engine.app import app


def test_openapi_and_discover_shell_are_served() -> None:
    with TestClient(app) as client:
        openapi = client.get("/v1/openapi.json")
        shell = client.get("/")

    assert openapi.status_code == 200
    assert openapi.json()["info"]["title"] == "Taste Engine"
    assert shell.status_code == 200
    assert "<title>Taste Engine</title>" in shell.text
    assert "Discover" in shell.text
