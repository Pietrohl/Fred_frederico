import os

from flask import Flask,jsonify
from fred_app.database.list_repository import ListRepository
from fred_app.database.sqlite_connection import connection
from fred_app.models.interfaces.FredAppException import FredAppException





def create_app(test_config=None):
    
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    db_connection = None
    
    with app.app_context():
        if test_config:
            db_connection = test_config['connection']
        else:
            db_connection = connection

        listRepository = ListRepository(db_connection)
    
        app.config.update({
            "connection": db_connection,
            "list_repository": listRepository
        })

        from fred_app.routes import list
        app.register_blueprint(list.list_bp)

    return app