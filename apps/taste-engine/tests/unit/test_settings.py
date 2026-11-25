import pytest

from taste_engine.settings import Settings, get_settings


def test_settings_read_environment_with_safe_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://unit@localhost/db")
    monkeypatch.setenv("AUTH_MODE", "passphrase")
    monkeypatch.setenv("PUBLIC_BASE_URL", "http://localhost:8000")
    monkeypatch.setenv("CATALOG_USER_AGENT", "taste-engine-test/0.1")

    settings = Settings()

    assert settings.cloud_ai_consent is False
    assert settings.region == "US"
    assert settings.availability_provider == "none"


def test_settings_fail_with_names_of_missing_required_variables(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in (
        "DATABASE_URL",
        "AUTH_MODE",
        "PUBLIC_BASE_URL",
        "CATALOG_USER_AGENT",
    ):
        monkeypatch.delenv(name, raising=False)
    get_settings.cache_clear()

    with pytest.raises(
        RuntimeError,
        match="AUTH_MODE.*CATALOG_USER_AGENT.*DATABASE_URL.*PUBLIC_BASE_URL",
    ):
        get_settings()

    get_settings.cache_clear()
