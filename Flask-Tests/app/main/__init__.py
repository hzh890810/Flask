from flask import Blueprint
name = "main"
bp = Blueprint(name,
               __name__,
               url_prefix='/',
               )
from .view import *