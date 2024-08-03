"""File for managing application environment variables."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DotEnv(BaseSettings):
    """Class for managing application environment variables."""

    # flake8: noqa: E501
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    sqlite_file_name: str = Field(default=...)


env = DotEnv()
