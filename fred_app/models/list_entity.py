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
        return self.name
