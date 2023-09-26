from flask import redirect, url_for, render_template, request, Response

from app.models.dojo import Dojo
from app.models.ninja import Ninja
from app.controllers.forms import DojoForm, NinjaForm

def index() -> Response:
    """Redirects to the listing of all dojos."""
    return redirect(url_for("dojo.list_all"))

def display_dojos() -> str:
    """
    Renders the main page displaying all dojos and a form to create a new dojo.

    Returns:
        render_template: Renders the 'index.html' template with all dojos and a creation form.
    """
    form = DojoForm()
    dojos = Dojo.get_all()

    return render_template("index.html", dojos=dojos, form=form)

def add_dojo() -> Response:
    """
    Adds a new dojo to the database and redirects to the main page.

    Returns:
        redirect: Redirects to the main page.
    """
    Dojo.save(request.form.to_dict())

    return redirect(url_for("dojo.list_all"))

def ninjas_per_dojo(id: int) -> str:
    """
    Render a template displaying a specific dojo and its associated ninjas.

    Args:
        id (int): The ID of the dojo.

    Returns:
        render_template: Renders the "dojo.html" template with the specified dojo and its ninjas.
    """
    data = {"id": id}
    dojo = Dojo.get_by_id(data)
    ninjas = Dojo.get_ninjas(data)

    return render_template("dojo.html", dojo=dojo, dojo_ninjas=ninjas)

def new_ninja() -> str:
    """
    Render a form to add a new ninja, with the dropdown choices for dojos dynamically populated.

    Returns:
        render_template: Renders the "add_ninja.html" template with the NinjaForm, 
                         where the 'dojo_id' field choices are set to all available dojos.
    """
    form = NinjaForm()
    form.dojo_id.choices = [(dojo.id, dojo.name) for dojo in Dojo.get_all()]
    return render_template("add_ninja.html", form=form)

def add_ninja() -> Response:
    """
    Save a new ninja to the database and redirect to the dojo's details page.

    Returns:
        redirect: Redirects to the details page of the dojo associated with the added ninja.
    """
    Ninja.save(request.form.to_dict())

    return redirect(url_for("dojo.details", id=request.form.get("dojo_id")))

