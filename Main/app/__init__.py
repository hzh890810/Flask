from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config
 
def create_app(config_name):
 
    app = Flask(__name__)
    app.config.from_object(config[config_name])
 
    """註冊擴充插件"""
    register_extensions(app)

    """註冊藍圖"""
    register_blueprints(app)
    return app

"""註冊擴充插件"""
def register_extensions(app):
    """Register extensions with the Flask application."""
    SQLAlchemy().init_app(app)

"""註冊藍圖"""
def register_blueprints(app):
    """Register blueprints with the Flask application."""
    import app.view as view
    view.init_app(app)