from http import HTTPStatus
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask,jsonify
from fred_app.database.list_repository import ListRepository
from fred_app.database.sqlite_connection import connection
from fred_app.models.interfaces.FredAppException import FredAppException


def init_openapi_spec(app):
    
        
    
    spec = APISpec(
    title="Fred Frederico app API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin()],
)
    
    
    with app.test_request_context():
        spec.path(view=app.view_functions['list.get_list'])
        spec.path(view=app.view_functions['list.get_lists'])
        spec.path(view=app.view_functions['list.create_list'])
        spec.path(view=app.view_functions['list.delete_list'])
        spec.path(view=app.view_functions['list.update_list'])
    
    print(spec.to_yaml())
        
    
    
    
    

    
    

def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)


    db_connection = None
    
    with app.app_context():
        
        
        # Seting Mock data for testing
        if test_config:
            db_connection = test_config['connection']
        else:
            db_connection = connection
    
        # Set app configuration
        app.config.update({
            "connection": db_connection,
            "list_repository": ListRepository(db_connection)
        })

        # Register modules to the app 
        from fred_app.routes import list
        app.register_blueprint(list.list_bp)

    def exception_handler(error: FredAppException):
        
        error_message = error.message or 'Error processing request'
        error_status = error.status_code or HTTPStatus.INTERNAL_SERVER_ERROR
        
        response = jsonify(error_message)
        response.status_code = error_status
        return response

    app.register_error_handler(Exception, exception_handler)

    init_openapi_spec(app)

    return app