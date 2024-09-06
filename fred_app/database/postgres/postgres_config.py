import psycopg2 
import os

schema_file_path = "fred_app/database/postgres/schema.sql"


f = open(schema_file_path, 'r') 
schema = f.read()


connection = psycopg2.connect(host=os.environ['POSTGRES_HOST'],
                            database=os.environ['POSTGRES_DB'],
                            port=os.environ['POSTGRES_PORT'],
                            user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASSWORD'])

cur = connection.cursor()
cur.execute(schema)
connection.commit()
