from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///login.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'supersecretkey'
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
    cnf_password = db.Column(db.String(256), nullable = False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username} - {self.email} - {self.password} - {self.cnf_password}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cnf_password = request.form['cnf_password']

        if password != cnf_password:
            flash("Password and Confirm Password should be same")
            print("Passwords do not match")
            return redirect('/')       
        else:
            login=Login(username=username, email=email, password=password, cnf_password=cnf_password)  
            db.session.add(login)
            db.session.commit()
            flash("Registration Successful", "success")
            print("Registration Successful")
    allLogin = Login.query.all()
    print(allLogin)
    return render_template("home.html")

@app.route('/show')
def show():
    allLogin = Login.query.all()
    print(allLogin)
    return "This is show page"


if __name__ == "__main__":
    app.run(debug=True)
