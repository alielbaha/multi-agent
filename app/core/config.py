from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key = ""
    anthropic_api_key = ""
    market_data_api_key = ""

    class Config:
        env_file = ".env"


settings = Settings()
