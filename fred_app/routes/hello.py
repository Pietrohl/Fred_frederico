from flask import (
    Blueprint,
    request
)

from fred_app.controllers.hello import HelloController

bp = Blueprint('hello', __name__, url_prefix='/hello')


 # a simple page that says hello
bp.route('', methods=['GET'])(HelloController(request).hello)