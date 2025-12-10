import psycopg2
from psycopg2 import Error
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv()

@contextmanager
def get_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST"),
            dbname=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            sslmode="require"
        )
        yield conn
    except Error as e:
        print(f"Database connection error: {e}")
        raise
    finally:
        if conn:
            conn.close()