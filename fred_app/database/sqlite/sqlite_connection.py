import os
import sqlite3

schema_file_path = "./fred_app/database/sqlite/schema.sql"


f = open(schema_file_path, 'r') 
schema = f.read()


connection = sqlite3.connect(os.environ['SQLITE3_DB'], 
                                        check_same_thread=False)

connection.execute(schema)
connection.commit()
    
