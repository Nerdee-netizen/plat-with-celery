import os

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USERNAME: str
    REDIS_PASSWORD: str
    REDIS_TASK_QUEUE_DB: int
    REDIS_NOTIFICATION_DB: int


class LocalDevSettings(EnvSettings):
    model_config = SettingsConfigDict(env_file="config", extra="ignore")


class DeployedSettings(EnvSettings):
    pass


def find_config() -> EnvSettings:
    if os.getenv("ENV"):
        return DeployedSettings()

    return LocalDevSettings()


env = find_config()

if __name__ == "__main__":
    print(env)