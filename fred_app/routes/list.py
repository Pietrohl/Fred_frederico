from flask import (
    Blueprint,
    request
)

from fred_app.controllers.list_controller import ListController
from fred_app.database.list_repository import ListRepository
from fred_app.services.list_service import ListService
from fred_app.database.sqlite_connection import connection


list_repo = ListRepository(db_connection=connection)
list_service = ListService(list_repo)



list_bp = Blueprint('list', __name__, url_prefix='/list')



list_bp.route('/', methods=['GET'])(ListController(request, list_service).get_lists)
list_bp.route('/<int:id>', methods=['GET'])(ListController(request, list_service).get_list)
list_bp.route('/', methods=['POST'])(ListController(request, list_service).create_list)
list_bp.route('/<name>', methods=['DELETE'])(ListController(request, list_service).delete_list)
list_bp.route('/<int:id>', methods=['PUT'])(ListController(request, list_service).update_list)