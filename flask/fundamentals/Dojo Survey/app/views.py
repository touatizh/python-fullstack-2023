from .forms import SurveyForm
from flask import request, render_template
def index():
    form = SurveyForm()
    return render_template("index.html", form=form)