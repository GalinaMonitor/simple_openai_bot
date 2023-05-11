from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_token: str
    bot_token: str


settings = Settings(".env")
