from flask import render_template,redirect,request,flash,url_for
from flask_login import LoginManager,current_user,logout_user,login_required,login_user
import app.model as model
from flask_login import UserMixin

Login_Manager = LoginManager()
Login_Manager.login_view = 'login'
Login_Manager.login_message = 'Please Login'
Login_Manager.login_message_category  = 'warning'

class User(UserMixin):  
    pass

def init_app(app):
    Login_Manager.init_app(app)

    @app.route("/creator")
    def creator():
        return model.creator
    
    @Login_Manager.user_loader  
    def user_loader(email):  
        if email not in model.USERS:  
            return  
    
        user = User()  
        user.id = email  
        return user  

    @app.route('/login',methods=["GET","POST"])
    def login():
        if(current_user.is_active):
            return redirect(request.args.get('next') or url_for('home'))
        if request.method == 'GET':  
            return render_template('login.html')

        form = request.form.to_dict()
        if form["account"] != '' and form["password"] !='':
            if form["account"] in model.USERS and request.form['password'] == model.USERS[form["account"]]['password']:   
                user = model.User()  
                user.id = form["account"]  
                login_user(user)  
                return redirect(request.args.get('next') or url_for('home'))
        flash('Wrong account or Password','error')
        return redirect(url_for('login'))
        
    @app.route('/')
    def home():
        return render_template("Home.html")

    @app.route('/protect')
    @login_required
    def protect():
        if current_user.is_active:  
            return 'Logged in as: ' + current_user.id + 'Login is_active:True'
        
    @app.route('/logout')  
    def logout():  
        logout_user()
        flash("Logged out",'info')
        return redirect(url_for("login"))