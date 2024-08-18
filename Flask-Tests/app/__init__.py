from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import config
 
def create_app(config_name):
 
    app = Flask(__name__)
    app.config.from_object(config[config_name])
 
    register_extensions(app)
    register_blueprints(app)
    return app

"""註冊擴充插件"""
def register_extensions(app):
    SQLAlchemy().init_app(app)

"""註冊藍圖"""
def register_blueprints(app):
    import app.view as view
    view.init_app(app)