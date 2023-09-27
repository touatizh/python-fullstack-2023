from flask import render_template, request, redirect, url_for, session
from app.controllers.forms import RegForm
from app.models.users import User

def index():
    """
    Render the main index page with the registration form.

    If there's any form data stored in the session (possibly from a previous failed 
    validation attempt), it pre-populates the registration form with that data.

    Returns:
        render_template: Renders the "index.html" template with the registration form.
    """
    
    forms = {"register": RegForm() if not "form_data" in session else RegForm(data=session["form_data"]),}
    session.pop('form_data', None)
    return render_template("index.html", forms=forms)

def register():
    """
    Process the registration form submission.

    Validates the registration form data. If the data is invalid, it stores the form data 
    in the session and redirects back to the index page. If the data is valid, it saves 
    the new user to the database and redirects back to the index page.

    Returns:
        redirect: Redirects to the index page.
    """
    form = RegForm(request.form)
    if not form.validate_on_submit():
        session["form_data"] = request.form
        return redirect(url_for("reg_log.home"))
    
    User.save(request.form.to_dict())
    return redirect(url_for("reg_log.home"))
