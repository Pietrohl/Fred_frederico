
from fred_app.database.connection import Connection
from fred_app.models.list.list_entity import List as ListEntity
from fred_app.models.list.new_list_dto import NewListDTO

class ListRepository:
    def __init__(self, db_connection: Connection):
        self.db= db_connection

    def create_list(self, list: NewListDTO) -> ListEntity:
        cur = self.db.cursor()
        cur.execute("INSERT INTO lists (name, owner, done) VALUES (?, ?, ?);", (list.name, 0, False))
        id = cur.lastrowid
        list= self.get_list(id=id, cur=cur)
        self.db.commit()
        return list
    
    def update_list(self, list: ListEntity) -> ListEntity:
        cur = self.db.cursor()
        cur.execute("UPDATE lists SET name = ?, done = ? WHERE id = ?", (list.name, list.done, list.id))
        count = cur.rowcount

        if count <= 0:
            raise KeyError(f"Key {list.id} not found in database")
        
        list= self.get_list(id=list.id)
        self.db.commit()
        return list

    def delete_list(self, id: int) -> bool:
        cur = self.db.cursor()
        cur.execute("DELETE FROM lists WHERE id = ?", (id))
        count = cur.rowcount
        
        if count <= 0:
            raise KeyError(f"Key {list.id} not found in database")
        
        self.db.commit()
        

    
    def get_list(self, id, cur = None):
        if (cur == None):
            cur = self.db.cursor()
            
        cur.execute("SELECT id, name, datetime(created_at, 'unixepoch', 'localtime') as date, owner, done from lists WHERE id = ?", (id,))
        row = cur.fetchone()
        
        return ListEntity(id=row[0], name=row[1], date=row[2], owner=row[3], done=row[4], items=[])

    def get_all_lists(self):
        cur = self.db.cursor()
        cur.execute("SELECT id, name, created_at, owner, done from lists;")
        rows = cur.fetchall()
        return map(lambda row : ListEntity(id=row[0], name=row[1], date=row[2], owner=row[3], done=row[4], items=[]), rows)