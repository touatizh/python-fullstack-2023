from flask import (Response, flash, redirect, render_template, request,
                   session, url_for)

from app import app
from app.models.user import User


@app.route("/")
def index() -> str:

    return render_template("index.html")

@app.route("/register/", methods=["POST"])
def register() -> Response:

    data = request.form.to_dict()

    if User.validate_registration(data):
        user = User.create(data)
        flash("Registred successfully. Proceed to login #reg", "info") if user else flash("Internal server error #reg", "danger")

    return redirect(url_for("index"))

@app.route("/login/", methods=["POST"])
def login() -> Response:

    data = request.form.to_dict()
    valid, user = User.validate_login(data)
    if valid:
        session["user_id"] = user.id

    return redirect(url_for("dashboard"))

@app.route("/logout/")
def logout() -> Response:

    session.pop("user_id")
    return redirect(url_for("index"))
