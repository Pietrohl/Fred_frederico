from fred_app.database.list_repository import ListRepository
from fred_app.models.list_entity import List
from fred_app.models.new_list_dto import NewListDTO

class ListService:
    def __init__(self, list_repository: ListRepository):
        self.list_repository = list_repository
    
    def create_list(self, new_list: NewListDTO) -> List:
        list = self.list_repository.create_list(new_list)
        list.append_to_name(' (NEW) ')
        self.list_repository.update_list(list)
        return list

    def get_all_lists(self):
        return ListRepository.get_all_lists(self)
    
    def update_list(self, list: List) -> List:
        return ListRepository.update_list(self, list)
    
    def get_list(self, list: List) -> List:
        return ListRepository.get_list(self, list)
