import os

from flask import Flask
from  fred_app.routes import  hello


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)


    app.register_blueprint(hello.bp)

    return app