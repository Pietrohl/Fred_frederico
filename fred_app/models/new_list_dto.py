class NewListDTO:
    def __init__(self, name: str = None):
        if name is None:
            raise ValueError("Name is required")
        

        self.name = name