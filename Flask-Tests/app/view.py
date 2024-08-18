from flask import render_template
import app.model as model
from flask_login import LoginManager,current_user,logout_user,login_required,login_user

Login_Manager = LoginManager()
Login_Manager.login_view = 'login'
Login_Manager.login_message = 'Please Login'

def init_app(app):
    Login_Manager.init_app(app)
    
    @app.route("/")
    def home():
        return render_template("Home.html")
    
    @app.route("/creator")
    def creator():
        return model.CREATOR