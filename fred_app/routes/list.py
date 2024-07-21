from flask import (
    Blueprint,
    current_app,
    request
)

from fred_app.controllers.list_controller import ListController
from fred_app.services.list_service import ListService


list_service = ListService(current_app.config['list_repository'])

list_bp = Blueprint('list', __name__, url_prefix='/list')



list_bp.route('/', methods=['GET'])(ListController(request, list_service).get_lists)
list_bp.route('/<int:id>', methods=['GET'])(ListController(request, list_service).get_list)
list_bp.route('/', methods=['POST'])(ListController(request, list_service).create_list)
list_bp.route('/<int:id>', methods=['DELETE'])(ListController(request, list_service).delete_list)
list_bp.route('/<int:id>', methods=['PUT'])(ListController(request, list_service).update_list)