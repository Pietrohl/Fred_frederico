from http import HTTPStatus
from flask import Request 
from fred_app.services.list_service import ListService
from fred_app.models.list.new_list_dto import NewListDTO
from fred_app.models.list.list_entity import List
from fred_app.models.list.update_list_dto import UpdateListDTO
from fred_app.models.interfaces.FredAppException import FredAppException

class ListController:
    def __init__(self, request: Request, list_service: ListService):
        self.request = request
        self.service = list_service

    def create_list(self):
        try:
            new_list = NewListDTO(name = self.request.json['name'])
        except Exception as err:
            print("ERROR: Error Creating list Invalid body ", err)
            raise FredAppException('Invalid body', HTTPStatus.BAD_REQUEST)


        list = self.service.create_list(new_list)
        return vars(list), HTTPStatus.CREATED


    
    def get_list(self, id):
        try:
            list = self.service.get_list(id)
            return vars(list), 200
        except Exception as err:
            print("ERROR: Error fetching list", err)
            raise FredAppException('List Not Found', HTTPStatus.NOT_FOUND)
    
    def update_list(self, id):

        updated_list = None
        try:
            updated_list = UpdateListDTO(name = self.request.json['name'], done = self.request.json['done'], owner = self.request.json['owner'], items = self.request.json['items'])
        
        except Exception as err:
            raise FredAppException('Invalid body', HTTPStatus.BAD_REQUEST)
        
        try:
            updated_list = self.service.update_list(id = id,name = updated_list.name, done = updated_list.done, owner = updated_list.owner, items = None)
            if not(updated_list):
                raise FredAppException('List Not Found', HTTPStatus.NOT_FOUND)            
            return vars(updated_list), 200
        except Exception as err:
            print("ERROR: Error updating list", err)
            raise FredAppException('Error updating list', HTTPStatus.INTERNAL_SERVER_ERROR)

    def delete_list(self, id):
        try:
            self.service.delete_list(id)
            return '',200
        except Exception as err:
            print("ERROR: Error deleting list", err)
            raise FredAppException('List Not Found', HTTPStatus.NOT_FOUND)

    def get_lists(self):
        return [vars(list) for list in self.service.get_all_lists()], 200
