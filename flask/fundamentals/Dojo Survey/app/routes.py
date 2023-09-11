from flask import Blueprint
from . import views

bp = Blueprint("dojo_survey", __name__)

bp.add_url_rule("/", "index", view_func=views.index)
bp.add_url_rule("/process", "process", view_func=views.process, methods=["POST"])
bp.add_url_rule("/result", "result", view_func=views.result)
