from flask import Request
from fred_app.services.list_service import ListService
from fred_app.models.list.new_list_dto import NewListDTO 

class ListController:
    def __init__(self, request: Request, list_service: ListService):
        self.request = request
        self.service = list_service

    def create_list(self):
        
        new_list = NewListDTO(name=self.request.json['name'])
        
        list =  self.service.create_list(new_list)
        
        return vars(list), 201
    
    def get_lists(self):
        return [vars(list) for list in self.service.get_all_lists()], 200
    
    def get_list(self, id):
        
        return vars(self.service.get_a_list(id)), 200