from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf8'
    )
    ACCESS_KEY: str
    PROXY_SERVICE_URL: str
