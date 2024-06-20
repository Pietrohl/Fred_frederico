from flask import Request 
from fred_app.services.list_service import ListService
from fred_app.models.new_list_dto import NewListDTO
from fred_app.models.list_entity import List

class ListController:
    def __init__(self, request: Request, list_service: ListService):
        self.request = request
        self.service = list_service

    def create_list(self):
        new_list = NewListDTO(name = self.request.json['name'])
        list = self.service.create_list(new_list)
        return vars(list), 201
    
    def get_list(self, id):
            list = self.service.get_list(id)
            return vars(list), 200
    
    def update_list(self, id):
        try:         
            updated_list = self.service.update_list(List(id = id,name = self.request.json['name'], date = self.request.json['done'], owner = self.request.json['owner'], done = None, items = None))
            
            if not(updated_list):
                return '',404           
            return vars(updated_list), 200
        except Exception as err:
            print("ERROR: ", err)
        except:
            raise KeyError (f"Key {id} not found in database")

    def delete_list(self, id):
        try:
            self.service.delete_list(id)
            return '',200
        except Exception as err:
            print("ERROR: ", err)
            return '',404

    def get_lists(self):
        return [vars(list) for list in self.service.get_all_lists()], 200
