from fred_app.database.list_repository import ListRepository
from fred_app.models.list.list_entity import List
from fred_app.models.list.new_list_dto import NewListDTO


class ListService:
    def __init__(self, list_repository: ListRepository):
        self.list_repository = list_repository

    def create_list(self, new_list: NewListDTO) -> List:
             
        list = self.list_repository.create_list(new_list)
        list.append_to_name(' (NEW)') 
        self.list_repository.update_list(list)
        return  list
             
    def get_all_lists(self):
        return self.list_repository.get_all_lists()   
    
    def get_a_list(self, id):
        return self.list_repository.get_a_list(id)