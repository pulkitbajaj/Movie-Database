from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///login.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fname = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(200), nullable=False)
#     password = db.Column(db.String(200), nullable=False)

#     def __repr__(self) -> str:
#         return f"{self.fname} - {self.email} - {self.password}"

class Login(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(250), nullable = False)
    password = db.Column(db.String(256), nullable = False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username} - {self.email}"

@app.route('/')
def home():
    login=Login(username="abcd", email="abc@gmail.com", password="abc123")                           
    db.session.add(login)
    db.session.commit()
    return render_template("home.html")

@app.route('/show')
def show():
    allLogin = Login.query.all()
    print(allLogin)
    return "This is show page"


if __name__ == "__main__":
    app.run(debug=True)
