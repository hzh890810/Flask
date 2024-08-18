from . import bp
from .form import *
from .model import *
from flask import render_template

@bp.route("/")
def home():
    return render_template("Home.html")