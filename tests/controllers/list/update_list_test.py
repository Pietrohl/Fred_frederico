import pytest
from fred_app.models.list.list_entity import List
from fred_app.models.list.update_list_dto import UpdateListDTO
import json



@pytest.fixture(autouse=True)
def set_up_db(app):
    with app.app_context():
        app.config["connection"].execute("INSERT INTO lists (name, owner, done) VALUES ('Test List', 1, FALSE);")
        app.config["connection"].commit()
    



def test_get_lists(client):
    
    update_list = UpdateListDTO(name = "Update List", done = True, owner = 0, items = [])
    
    response = client.put("/list/1", data=json.dumps(vars(update_list)), content_type='application/json')
    
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert data.get("name") == "Update List"
    assert data.get("done") == True
    assert data.get("owner") == 0
    assert data.get("items") == []