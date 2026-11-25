from functools import lru_cache

from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_file=None, extra="ignore")

    database_url: str = Field(validation_alias="DATABASE_URL")
    auth_mode: str = Field(validation_alias="AUTH_MODE")
    public_base_url: str = Field(validation_alias="PUBLIC_BASE_URL")
    cloud_ai_consent: bool = Field(default=False, validation_alias="CLOUD_AI_CONSENT")
    llm_base_url: str | None = Field(default=None, validation_alias="LLM_BASE_URL")
    stt_url: str | None = Field(default=None, validation_alias="STT_URL")
    availability_provider: str = Field(default="none", validation_alias="AVAILABILITY_PROVIDER")
    availability_api_key: str | None = Field(default=None, validation_alias="AVAILABILITY_API_KEY")
    catalog_user_agent: str = Field(validation_alias="CATALOG_USER_AGENT")
    region: str = Field(default="US", validation_alias="REGION")


@lru_cache
def get_settings() -> Settings:
    try:
        return Settings()  # type: ignore[call-arg]
    except ValidationError as exc:
        missing = sorted(
            str(error["loc"][0])
            for error in exc.errors()
            if error["type"] == "missing"
        )
        if missing:
            raise RuntimeError(
                f"Missing required environment variables: {', '.join(missing)}"
            ) from exc
        raise
