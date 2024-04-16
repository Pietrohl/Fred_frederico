from flask import (
    Blueprint
)


bp = Blueprint('hello', __name__, url_prefix='/hello')


 # a simple page that says hello
@bp.route('', methods=['GET'])
def hello():
    return 'Hello, World!'

