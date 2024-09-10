import pytest
from fred_app.models.list.list_entity import List
from fred_app.models.list.new_list_dto import NewListDTO
import json  

def test_post_list(client):
    
    list = NewListDTO(name = "Test List")
    
    response = client.post("/list/", data=json.dumps(vars(list)), content_type='application/json')
    assert response.status_code == 201