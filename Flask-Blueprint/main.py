from flask import Flask,render_template

app = Flask(__name__)

def register_blueprints(app):
    from blueprint import bp
    app.register_blueprint(bp)
# 首頁
@app.route("/")
def Home():
  return "Main Page"

@app.route("/index")
def index():
  return render_template("index.html")

register_blueprints(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4034,debug=True)