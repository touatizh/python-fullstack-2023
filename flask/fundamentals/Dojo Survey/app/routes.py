from flask import Blueprint
from . import views

bp = Blueprint("dojo_survey", __name__)

bp.add_url_rule("/", "index", view_func=views.index)