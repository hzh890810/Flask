from flask import Flask,url_for,redirect,render_template,request,flash,send_from_directory
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './static/assets/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'

@app.route('/user/<string:name>')
def username(name):
    return 'i am ' + name

@app.route("/age/<int:age>")
def name(age):
    return 'i am ' + str(age) + ' years old'

@app.route('/pageA')
def A():
    return 'here is a'

@app.route('/pageB')
def b():
    #  所得結果為'/pagrA'
    return url_for('A')

@app.route('/pageC')
def C():
    #  重新導向至 pageA
    return redirect(url_for('A'))

@app.route('/pageD',methods=["GET"])
def D():
    #  重新導向至 pageA
    return redirect("/pageA")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("Login.html")
    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        return redirect(url_for('welcome',**locals()))
    
@app.route('/')
@app.route('/welcome')
def welcome():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("Welcome.html",**locals())

def allowed_file(file):
    return '.' in file and \
           file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            print('No file part')
            return redirect(request.url)
        f = request.files['file']
        if f.filename == '':
            flash('No selected file')
            print('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return render_template("Upload.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4034,debug=True)