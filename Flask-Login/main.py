from flask import Flask,url_for,redirect,render_template,request,flash,send_from_directory
from flask_login import LoginManager,current_user,logout_user,login_required,login_user
import os
import model

Login_Manager = LoginManager()
app = Flask(__name__)
Login_Manager.init_app(app)
Login_Manager.login_view = 'login'
Login_Manager.login_message = 'Please Login'

app.secret_key =  os.urandom(16).hex()

users = {'A4034': {'password': 'A4034'}}  

@Login_Manager.user_loader  
def user_loader(email):  
    if email not in users:  
        return  
  
    user = model.User()  
    user.id = email  
    return user  

@app.route('/login',methods=["GET","POST"])
def login():
    if(current_user.is_active):
        return redirect(request.args.get('next') or url_for('home'))
    if request.method == 'GET':  
        return render_template('login.html')

    form = request.form.to_dict()
    if form["email"] != '' and form["password"] !='':
        if form["email"] in users and request.form['password'] == users[form["email"]]['password']:   
            user = model.User()  
            user.id = form["email"]  
            login_user(user)  
            return redirect(request.args.get('next') or url_for('home'))
    flash('Wrong Email or Password')
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
    return 'Logged out'  

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4034,debug=True)