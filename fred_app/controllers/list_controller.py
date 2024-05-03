from flask import Request
from fred_app.services.list_service import ListService
from fred_app.models.list.new_list_dto import NewListDTO 

class ListController:
    def __init__(self, request: Request, list_service: ListService):
        self.request = request
        self.service = list_service

    def create_list(self):
        
        try:
            new_list = NewListDTO(name=self.request.json['name'])
            list =  self.service.create_list(new_list)
            return vars(list), 201
        except:
            return "Error creating the list", 400
    
    
    def get_lists(self):
        
        try:
            all_lists = self.service.get_all_lists()
            return [vars(list) for list in all_lists], 200
    
        except:
            return "Error fetching the lists", 404
    
    
    def get_list(self, id):
        
        try:
            list = self.service.get_a_list(id)
            return vars(list), 200
            
        except:
            return "List not found", 404    