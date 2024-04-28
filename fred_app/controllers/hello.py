from flask import Request 

class HelloController:
    def __init__(self, request: Request):
        self.request = request
        

    def hello(self):
        return 'Hello, World!'

