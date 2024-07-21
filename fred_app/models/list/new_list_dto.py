from fred_app.models.list.list_entity import List

class NewListDTO:
    name: str = None
        
    def __init__(self, name: str = None):
        
        if name is None:
            raise ValueError("Name is required")
        
        self.name = name