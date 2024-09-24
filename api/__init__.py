from flask import Blueprint

api = Blueprint('api', __name__)

from . import user, search, video, common_api, recommend, live_api