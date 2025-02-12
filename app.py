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

    def _repr_(self) -> str:
        return f"{self.sno} - {self.username} - {self.email}"

@app.route('/')
def home():
    # user = User(fname="abcd", email="abc@gmail.com", password="abc123")
    login=Login(username="abcd", email="abc@gmail.com", password="abc123")                           
    db.session.add(login)
    db.session.commit()
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fr.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)

# class Fr(db.Model):
#     sno = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(150), nullable = False)
#     email = db.Column(db.String(250), nullable = False)
#     password = db.Column(db.String(256), nullable = False)

#     def _repr_(self) -> str:
#         return f"{self.sno} - {self.username} - {self.email}"


# @app.route('/', methods = ['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         fr = Fr(username = username, email = email, password = password)
#         db.session.add(fr)
#         db.session.commit()
#     allFr = Fr.query.all()
#     return render_template('index.html', allFr=allFr)

# @app.route('/show')
# def show():
#     allFr = Fr.query.all()
#     print(allFr)
#     return "this is show"

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)