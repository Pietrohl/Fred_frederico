from flask import (
    Blueprint,
    request
)

from fred_app.database.list_repository import ListRepository
from fred_app.controllers.list_controller import ListController
from fred_app.services.list_service import ListService

list_db = []
list_repo = ListRepository(list_db)
list_service = ListService(list_repo)



list_bp = Blueprint('list', __name__, url_prefix='/list')


list_bp.route('/', methods=['POST'])(ListController(request,list_service).create_list)
list_bp.route('/', methods=['GET'])(ListController(request,list_service).get_lists)
