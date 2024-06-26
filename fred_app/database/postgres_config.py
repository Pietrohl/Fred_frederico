import psycopg2 
from psycopg2.extras import DictCursor
import os

schema_file = f"$HOME/fred_app/database/schema.sql"

conn = psycopg2.connect(host='localhost',
                        datbase='fred',
                        user=os.environ['POSTGRES_USER'],
                        password=s.environ['POSTGRES_PASSWORD'])

cursor = conn.cursor(cursor_factory=DictCursor)

with open(schema_file, 'r') as f:
    schema = f.read()

cursor.execute(schema)
conn.commit()