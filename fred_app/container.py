from dependency_injector import containers, providers
from  fred_app.services import hello


class Container(containers.DeclarativeContainer):
    
    hello_service = providers.Factory(hello.HelloService)
    