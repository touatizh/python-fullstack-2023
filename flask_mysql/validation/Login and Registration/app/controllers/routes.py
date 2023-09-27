from flask import Blueprint
from app.controllers import views
bp = Blueprint("reg_log", __name__)

bp.add_url_rule("/", "home", view_func=views.index)
bp.add_url_rule("/register", "register", view_func=views.register, methods=["POST"])