"""Core file to handle database connection."""

from sqlmodel import SQLModel, create_engine, Session
from src.core.environment import env

sqlite_url = f"sqlite:///{env.sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_database_and_tables() -> None:
    """Method to create database and tables."""

    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
