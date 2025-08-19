from typing import Any

from app.db import SessionLocal


def get_database() -> Any:
    database = SessionLocal()

    try:
        yield database
    finally:
        database.close()
