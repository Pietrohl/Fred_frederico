from datetime import date
from sqlite3 import Connection
from fred_app.models.list_entity import List as ListEntity
from fred_app.models.new_list_dto import NewListDTO

class ListRepository:
    def __init__(self, db_connection: Connection):
        self.db = db_connection

    def create_list(self, list: NewListDTO) -> ListEntity:
        cur = self.db.cursor()
        id = cur.execute("INSERT INTO lists (name, owner, done) VALUES (?, ?, ?);", (list.name, 0, False)).lastrowid
        list= self.get_list(id=id, cur=cur)
        self.db.commit()
        return list
    
    def update_list(self, list: ListEntity) -> ListEntity:
        cur = self.db.cursor()
        id = cur.execute("UPDATE lists SET name = ?, done = ? WHERE id = ?", (list.name, list.done, list.id)).lastrowid
        list= self.get_list(id=id, cur=cur)
        self.db.commit()
        return list

    def delete_list(self, list: ListEntity) -> ListEntity:
        self.db[list.id].remove(list)

        return list
    
    def get_list(self, id, cur = None):
        if (cur == None):
            cur = self.db.cursor()
            
        row = cur.execute("SELECT id, name, datetime(created_at, 'unixepoch', 'localtime') as date, owner, done from lists WHERE id = ?", (id,)).fetchone()
        return ListEntity(id=row[0], name=row[1], date=row[2], owner=row[3], done=row[4], items=[])

    def get_all_lists(self):
        cur = self.db.cursor()
        rows = cur.execute("SELECT id, name, datetime(created_at, 'unixepoch', 'localtime') as date, owner, done from lists").fetchall()
        return map(lambda row : ListEntity(id=row[0], name=row[1], date=row[2], owner=row[3], done=row[4], items=[]), rows)