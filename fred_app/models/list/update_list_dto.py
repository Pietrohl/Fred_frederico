class UpdateListDTO:
    def __init__(self, name, done, owner, items):
            
        if  name is None:
            raise ValueError("Name is required")
        
        if done is None:
            raise ValueError("Done is required")
        
        if  owner is None:
            raise ValueError("Owner is required")

        if items is None:
            raise ValueError("Items is required")
                                
        self.name = name
        self.done = done
        self.owner = owner
        self.items = items