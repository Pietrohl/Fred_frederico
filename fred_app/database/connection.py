
from abc import ABC
import psycopg2

# Generic Connection class that implements PEP 249 Pyrhon Database API Specification v2.0
class Connection(ABC,psycopg2.extensions.connection):
    pass


class ConnectionFactory():
    def __init__(self, db_type: str = "sqlite3"):
        self.db_type = db_type

    def create_connection(self) -> Connection:
        if self.db_type == "sqlite3":
            from fred_app.database.sqlite.sqlite_connection import connection
        elif self.db_type == "postgres":
            from fred_app.database.postgres.postgres_config import connection
        else:
            raise ValueError("Invalid db type")
        
        return connection