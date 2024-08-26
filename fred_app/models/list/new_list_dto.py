class NewListDTO:
    json_schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            },
            "required": ["name"]
        }
        
    def __init__(self, name):
        
        if name is None:
            raise ValueError("Name is required")
        else:
            self.name = name
    

