from flask import Blueprint
from app.controllers import views as vw

# Create Blueprints objects to define routes
ninja = Blueprint("ninja", __name__)
dojo = Blueprint("dojo", __name__)

# Dojo related routes
dojo.add_url_rule("/", "home", view_func=vw.index)
dojo.add_url_rule("/dojos/", "list_all", view_func=vw.display_dojos)
dojo.add_url_rule("/dojo/create", "create", view_func=vw.add_dojo, methods=["POST"])
dojo.add_url_rule("/dojo/<int:id>/", "details", view_func=vw.ninjas_per_dojo)

# Ninja related routes
ninja.add_url_rule("/ninjas", "new_ninja", view_func=vw.new_ninja)
ninja.add_url_rule("/ninjas/create", "create", view_func=vw.add_ninja, methods=["POST"])