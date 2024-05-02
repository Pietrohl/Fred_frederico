from datetime import date
from fred_app.models.list.new_list_dto import NewListDTO
from fred_app.models.list.list_entity import List as ListEntity

class ListRepository:
    def __init__(self, db_connection = []):
        self.db = db_connection

    def create_list(self, list: NewListDTO) -> ListEntity:
        list = ListEntity(id = len(self.db), name = list.name, date = date.today(), owner = 0, done = False, items= [])
        self.db.append(list)   
            
        return list
    
    def update_list(self, list: ListEntity) -> ListEntity:
        self.db[list.id].name = list.name
        return self.db[list.id]
    
    def get_all_lists(self):
        return self.db