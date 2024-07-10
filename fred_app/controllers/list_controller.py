from flask import Request 
from fred_app.services.list_service import ListService
from fred_app.models.list.new_list_dto import NewListDTO
from fred_app.models.list.list_entity import List
from fred_app.models.list.update_list_dto import UpdateListDTO

class ListController:
    def __init__(self, request: Request, list_service: ListService):
        self.request = request
        self.service = list_service

    def create_list(self):
        new_list = NewListDTO(name = self.request.json['name'])
        list = self.service.create_list(new_list)
        return vars(list), 201
    
    def get_list(self, id):
        try:
            list = self.service.get_list(id)
            return vars(list), 200
        except Exception as err:
            print("ERROR: Error fetching list", err)
            return 'List not Found',404
    
    def update_list(self, id):
        try:
            updated_list = UpdateListDTO(name = self.request.json['name'], done = self.request.json['done'], owner = self.request.json['owner'], items = self.request.json['items'])
            updated_list = self.service.update_list(id = id,name = updated_list.name, done = updated_list.done, owner = updated_list.owner, items = None)
            
            if not(updated_list):
                return '',404           
            return vars(updated_list), 200
        except Exception as err:
            print("ERROR: Error updating list", err)
            return 'Error updating list',404

    def delete_list(self, id):
        try:
            self.service.delete_list(id)
            return '',200
        except Exception as err:
            print("ERROR: Error deleting list", err)
            return '',404

    def get_lists(self):
        return [vars(list) for list in self.service.get_all_lists()], 200
