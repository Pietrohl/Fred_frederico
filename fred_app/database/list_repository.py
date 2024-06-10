from datetime import date
from models.list_entity import List as ListEntity
from models.new_list_dto import NewListDTO

class ListRepository:
    def __init__(self, db_connection = []):
        self.db = db_connection

    def create_list(self, list: NewListDTO) -> ListEntity:
        list = ListEntity(id = len(self.db), name = list.name, date = date.today(), owner = 0, done = False, items = [])
        self.db.append(list)

        return list
    
    def update_list(self, list: ListEntity) -> ListEntity:
        self.db[list.id].name = list.name
        self.db[list.id]

    def delete_list(self, list: ListEntity) -> ListEntity:
        self.db[list.id].remove(list)

        return list


    def get_all_lists(self):
        return self.db

