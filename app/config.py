"""
This module contains the configuration settings for the application.
It uses the pydantic library to define the settings and load them from environment variables.

To override the settings, create a .env file in the root directory of the project and add the settings you want to override.
For example:
DEBUG=True
RELOAD=True
WORKERS=4
PORT=8001
DATABASE_URL=postgresql://user:passwd@host:port/db
OAUTH_TOKEN_SECRET=my_secret
"""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://user:passwd@host:port/db"
    debug: bool = True
    reload: bool = True
    host: str = "127.0.0.1"
    port: int = 8000
    workers: int = 4
    project_name: str = "Demo FastAPI project"
    oauth_token_secret: str = "my_secret"


load_dotenv()
settings = Settings()

__all__ = ["settings"]
