import pytest
from fred_app.models.list.list_entity import List
import json


@pytest.fixture(autouse=True)
def set_up_db(app):
    with app.app_context():
        app.config["connection"].execute("INSERT INTO lists (name, owner, done) VALUES ('Test List', 1, FALSE);")
        app.config["connection"].commit()
    



def test_get_lists(client):
    
    response = client.get("/list/1")
    data = json.loads(response.data.decode("utf-8")) 
    assert response.status_code == 200
    assert data.get("name") == "Test List"
    assert data.get("done") == False
    assert data.get("owner") == 0
    assert data.get("items") == []