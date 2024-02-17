from pydantic_settings import BaseSettings  # type: ignore


class Settings(BaseSettings):
    """Instance which imports and provides data from the .env file."""

    DB_HOST: str = str()
    DB_NAME: str = str()
    DB_USER: str = str()
    DB_PASSWORD: str = str()
    DB_PORT: str = str()
    DB_SSL_MODE: str = str()
    CONSUMER_API_KEY: str = str()
    CONSUMER_API_KEY_SECRET: str = str()
    ACCESS_TOKEN: str = str()
    ACCESS_SECRET: str = str()
    TWEET_FILTER: list = list()

    class Config:
        """Instance which imports data from .env file."""

        env_file = ".env"
