from http import HTTPStatus
from typing import Union
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask,jsonify, render_template
from fred_app.controllers.documentation import get_redoc
from fred_app.constants import OPENAPI_JSON_URL
from fred_app.database.list_repository import ListRepository
from fred_app.database.sqlite_connection import connection
from fred_app.models.common.FredAppException import FredAppException
from fred_app.models.list.new_list_dto import NewListDTO
from fred_app.models.list.list_entity import List
from fred_app.models.list.update_list_dto import UpdateListDTO


def init_openapi_spec(app):
    
    spec = APISpec(
    title="Fred Frederico app API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin()],
)
    
    with app.test_request_context():
    # Add components to spec
        spec.components.schema("ListItem", component={})
        spec.components.schema("NewListDTO", component=NewListDTO.json_schema)
        spec.components.schema("List", component=List.json_schema)
        spec.components.schema("UpdateListDTO", component=UpdateListDTO.json_schema)
        spec.components.schema("ErrorResponse", component=FredAppException.json_schema)
        spec.components.schema("ListId", component={"type": "integer"})
    # Add paths to the spec
        spec.path(view=app.view_functions['list.get_list'])
        spec.path(view=app.view_functions['list.get_lists'])
        spec.path(view=app.view_functions['list.create_list'])
        spec.path(view=app.view_functions['list.delete_list'])
        spec.path(view=app.view_functions['list.update_list'])
    
        app.config.update({
            "spec": spec
        })
        
        app.add_url_rule(OPENAPI_JSON_URL, 'openapi', spec.to_dict, methods=['GET'])
        
        app.route('/redoc', methods=['GET'])(get_redoc)
       
       
       
def register_route_modules(app):
    
    with app.app_context():
    # Register modules to the app 
        from fred_app.routes import list
        app.register_blueprint(list.list_bp)
    


def exception_handler(error: Union[FredAppException, any]):
    default_error_message = 'Error processing request'
    
    
    if(error != FredAppException):
        return jsonify(default_error_message), HTTPStatus.INTERNAL_SERVER_ERROR
    
    error_message = error.message or default_error_message
    error_status = error.status_code or HTTPStatus.INTERNAL_SERVER_ERROR
    
    response = jsonify(error_message)
    response.status_code = error_status
    return response
    
           
       
        
def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    db_connection = None
    
    with app.app_context():
        
        
        # Setting Mock data for testing
        if test_config:
            db_connection = test_config['connection']
        else:
            db_connection = connection
    
        # Set app configuration
        app.config.update({
            "connection": db_connection,
            "list_repository": ListRepository(db_connection)
        })

        

  
    register_route_modules(app)
    app.register_error_handler(Exception, exception_handler)
    init_openapi_spec(app)

    return app