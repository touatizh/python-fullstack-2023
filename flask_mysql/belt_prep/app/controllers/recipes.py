from flask import (Response, flash, redirect, render_template, request,
                   session, url_for)

from app import app
from app.models.recipe import Recipe
from app.models.user import User, login_required


@app.route("/dashboard")
@login_required
def dashboard():

    recipes = Recipe.get_all()
    user = User.get_by_id({"id": session.get("user_id")})
    return render_template("dashboard.html", recipes=recipes, current_user=user)

@app.route("/recipes/<int:id>/")
@login_required
def show_recipe(id):

    recipe = Recipe.get_by_id({"id": id})
    return render_template("show_recipe.html", recipe=recipe)

@app.route("/recipes/new")
@login_required
def new_recipe():

    return render_template("add_recipe.html", user_id=session.get("user_id"))

@app.route("/recipes/create", methods=["POST"])
@login_required
def create_recipe():

    if not Recipe.validate_data(request.form.to_dict()):
        return redirect(url_for("new_recipe"))
    
    Recipe.create(request.form.to_dict())
    return redirect(url_for("dashboard"))

@app.route("/recipes/edit/<int:id>/")
@login_required
def edit_recipe(id):

    recipe = Recipe.get_by_id({"id": id})
    return render_template("edit_recipe.html", recipe=recipe)

@app.route("/recipes/update", methods=["POST"])
@login_required
def update():

    if not Recipe.validate_data(request.form.to_dict()):
        return redirect(url_for("edit_recipe", id=request.form.get("id")))
    
    Recipe.update(request.form.to_dict())
    return redirect(url_for("dashboard"))

@app.route("/recipes/<int:id>/delete")
@login_required
def delete(id):

    Recipe.delete({"id": id})
    return redirect(url_for("dashboard"))