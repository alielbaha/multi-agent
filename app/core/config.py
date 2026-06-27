from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")

    groq_api_key: str
    market_data_api_key: str = ""


settings = Settings()
