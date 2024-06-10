from flask import (
    Blueprint,
    request
)

from controllers.list_controller import ListController
from database.list_repository import ListRepository
from services.list_service import ListService

list_db = []
list_repo = ListRepository(list_db)
list_service = ListService(list_repo)


list_bp = Blueprint('list', __name__, url_prefix='/list')



list_bp.route('/', methods=['GET'])(ListController(request, list_service).get_lists)
list_bp.route('/<int:id>', methods=['GET'])(ListController(request, list_service).get_list)
list_bp.route('/', methods=['POST'])(ListController(request, list_service).create_list)
list_bp.route('/<str:name>', methods=['DELETE'])(ListController(request, list_service).delete_list)
list_bp.route('/<int:id>', methods=['PUT'])(ListController(request, list_service).update_list)
