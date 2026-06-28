from flask import Flask, render_template, request
from models import db

app = Flask(__name__)

app.config["SECRET_KEY"] = "monsterboy123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
