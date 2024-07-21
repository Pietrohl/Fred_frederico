from fred_app.models.list.list_entity import List
import json

def test_get_lists(client):
    
    response = client.get("/list/")
    assert response.status_code == 200