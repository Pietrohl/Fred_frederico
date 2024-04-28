

from datetime import date
from fred_app.models.list.new_list_dto import NewListDTO
from fred_app.models.list.list_entity import List


class ListRepository:
    def __init__(self, db_connection = []):
        self.db = db_connection

    def create_list(self, list: NewListDTO) -> List:
        list = List(id = len(self.db), name = list.name, date = date.today(), owner = 0, done = False, list_repository = self)
        self.db.append(list)   
            
        return list
    
    def update_list(self, id, name):
        self.db[id].name = name
        return self.db[id]
    
    def get_all_lists(self):
        return [list.to_dict() for list in self.db]