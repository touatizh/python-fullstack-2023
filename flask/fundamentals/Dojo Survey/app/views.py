from .forms import SurveyForm
from flask import request, render_template, session, redirect, url_for

def index():
    form = SurveyForm()
    return render_template("index.html", form=form)

def process():
    session["name"] = request.form.get("name")
    session["location"] = request.form.get("location")
    session["fav_lang"] = request.form.get("fav_language")
    session["additional"] = request.form.get("additional")

    return redirect(url_for("result"))
