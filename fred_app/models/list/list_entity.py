


class List(object): 
    def __init__(self, id, name, date, owner, done, list_repository):
        self.id = id
        self.name: str = name
        self.date = date
        self.owner = owner
        self.done = done
        self.list_repository = list_repository


    def __repr__(self):
        return f'List(id={self.id}, name={self.name}, items={self.items}, date={self.date}, owner={self.owner}, done={self.done})'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'owner': self.owner,
            'done': self.done
        }

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['id'], adict['name'], adict['items'])
    
    
    def append_to_name(self, string):
        self.list_repository.update_list(self.id, self.name + string)
        return self.name