from . import bp
from .model import *
from flask import render_template

@bp.route("/")
def Home():
  return "Blueprint Page" 

@bp.route("/index")
def index():
  return render_template("blueprint/index.html")