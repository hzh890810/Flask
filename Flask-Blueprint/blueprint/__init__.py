from flask import Blueprint

bp = Blueprint("blueprint",
               __name__,
               url_prefix="/bp",
               template_folder='templates',
               static_folder='static'
               )

from .view import *