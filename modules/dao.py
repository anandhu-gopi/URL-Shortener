import os
import sqlite3
from sqlite3.dbapi2 import Connection

from modules.utils import Singleton


class DAO(metaclass=Singleton):
    """Used for accessing the database."""

    def __init__(self, db_name: str) -> None:
        self._db_name = db_name

    @property
    def connection(self) -> Connection:
        return sqlite3.connect(self._db_name)

    def run_ddl_file(self, file_path: str) -> None:
        if not os.path.exists(file_path):
            raise FileNotFoundError()
        with open(file_path) as fp:
            with self.connection as conn:
                conn.executescript(fp.read())


dao = DAO(os.getenv("DB_NAME", "database.db"))
