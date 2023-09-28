from app.controllers.forms import LoginForm, RegForm
from app.models.users import User

from flask import flash, redirect, render_template, request, session, url_for


def index():
    """
    Render the main index page with the registration form.

    If there's any form data stored in the session (possibly from a previous failed 
    validation attempt), it pre-populates the registration form with that data.

    Returns:
        render_template: Renders the "index.html" template with the registration form.
    """
    
    forms = {"register": RegForm() if not "form_data" in session else RegForm(data=session["form_data"]),
             "login": LoginForm()}
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
    
    session["user_id"] = User.save(request.form.to_dict())
    return redirect(url_for("reg_log.dashboard"))

def login():
    """
    Process the login form submission.

    Validates the login form data. If the data is invalid, it redirects back to the index page. 
    If the data is valid, it stores the user's ID in the session and redirects to the dashboard.

    Returns:
        redirect: Redirects to the index page if the form is invalid or the dashboard if the login is successful.
    """
    form = LoginForm(request.form)
    if not form.validate_on_submit():
        return redirect(url_for("reg_log.home"))
    
    user = User.get_by_email({"email": request.form.get("email")})
    session["user_id"] = user.id
    return redirect(url_for("reg_log.dashboard"))

def dashboard():
    """
    Render the dashboard page for the logged-in user.

    Checks if the user is logged in by verifying the presence of user_id in the session.
    If the user is not logged in, it redirects back to the index page with a flash message.
    If the user is logged in, it fetches the user's data and renders the dashboard page.

    Returns:
        render_template: Renders the "dashboard.html" template with the user's first name.
        redirect: Redirects to the index page if the user is not logged in.
    """
    if not session.get("user_id"):
        flash("Login first. #login", "danger")
        return redirect(url_for("reg_log.home"))
    
    user = User.get_by_id({"id": session["user_id"]})
    return render_template("dashboard.html", user_name=user.first_name)
