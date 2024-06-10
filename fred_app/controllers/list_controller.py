from flask import Request 
from fred_app.database.list_repository import ListService
from fred_app.models.new_list_dto import NewListDTO

class ListController:
    def __init__(self, request: Request, list_service: ListService):
        self.request = request
        self.service = list_service

    def create_list(self):
        new_list = NewListDTO(name = self.request.json['name'])
        list = self.service.create_list(new_list)
        return vars(list), 201

    
    def update_list(self):
        list = self.request.json['name']
        self.service.update_list(list)
        return [vars(list)], 200


    def delete_list(self, list):
        try:
            list = self.request.json['name']
            self.service.delete_list(list)
            return 200
        except Exception as err:
            print("ERROR: ", err)


    def get_list(self):
        return [vars(list) for list in self.service.get_all_lists()], 200
