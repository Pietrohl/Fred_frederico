class List(object): 
    def __init__(self, id, name, date, owner, done, items):
        self.id = id
        self.name: str = name
        self.date = date
        self.owner = owner
        self.done = done
        self.items = items

    
    def append_to_name(self, string):
        self.name = self.name + string
        return self
   
    def update(self, name, done, owner, items):
        self.name = name
        self.done = done
        self.owner = owner
        self.items = items
        return self