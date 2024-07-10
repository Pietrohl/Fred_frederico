import sqlite3
from flask import Flask
from flask.testing import FlaskClient
import pytest
from fred_app import create_app


def setup_mock_db():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE IF NOT EXISTS lists (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, created_at integer(4) not null default (strftime('%s', CURRENT_TIMESTAMP)) NOT NULL , owner INTEGER, done BOOLEAN);")
    db.commit()

    return db




@pytest.fixture()
def app():
    
    mock_db = setup_mock_db()
    
    test_config = {
        'connection': mock_db
    }
    
    app = create_app(test_config)
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()