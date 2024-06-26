from datetime import date
from fred_app.models.list.new_list_dto import NewListDTO
from fred_app.models.list.list_entity import List as ListEntity
from psycopg2 import connect

class ListRepository:
    def __init__(self, db_connection: connect):
        self.db = db_connection

    def create_list(self, list: NewListDTO) -> ListEntity:
        cur = self.db.cursor()
        id = cur.execute("INSERT INTO lists (name, owner, done) VALUES (?, ?, ?);", (list.name, 0, False)).lastrowid
        list= self.get_list(id=id, cur=cur)
        self.db.commit()
        return list
    
    def update_list(self, list: ListEntity) -> ListEntity:
        cur = self.db.cursor()
        id = cur.execute("UPDATE lists SET name = ?, done = ? WHERE id = ?", (list.name, list.done, list.id)).rowcount
        self.db.commit()

        if id == 0:
            raise KeyError(f"Key {list.id} not found in database")
        
        list= self.get_list(id=list.id)
        return list

    def delete_list(self, id: int) -> bool:
        cur = self.db.cursor()
        id = cur.execute("DELETE FROM lists WHERE id = ?", (id,)).rowcount
        self.db.commit()
        
        if id == 0:
            raise KeyError(f"Key {list.id} not found in database")
        

    
    def get_list(self, id, cur = None):
        if (cur == None):
            cur = self.db.cursor()
            
        row = cur.execute("SELECT id, name, datetime(created_at, 'unixepoch', 'localtime') as date, owner, done from lists WHERE id = ?", (id,)).fetchone()
        return ListEntity(id=row[0], name=row[1], date=row[2], owner=row[3], done=row[4], items=[])

    def get_all_lists(self):
        cur = self.db.cursor()
        rows = cur.execute("SELECT id, name, datetime(created_at, 'unixepoch', 'localtime') as date, owner, done from lists").fetchall()
        return map(lambda row : ListEntity(id=row[0], name=row[1], date=row[2], owner=row[3], done=row[4], items=[]), rows)