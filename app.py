from flask import Flask, render_template, request, redirect, flash, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///login.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'supersecretkey'
db = SQLAlchemy(app)

# Model for Login
class Login(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    cnf_password = db.Column(db.String(256), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username} - {self.email} - {self.password} - {self.cnf_password}"

# Model for Signup
class Signup(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} -  {self.email} - {self.password} "

# Model for Search
class Search(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie = db.Column(db.String(150), nullable=False)
    date_searched = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.movie} - {self.date_searched}"

# Route for home page (signup)
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':    
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cnf_password = request.form['cnf_password']

        if password != cnf_password:
            flash("Password and Confirm Password should be same")
            print("Passwords do not match")
            return redirect('/home')       
        else:
            login = Login(username=username, email=email, password=password, cnf_password=cnf_password)  
            db.session.add(login)
            db.session.commit()
            flash("Registration Successful", "success")
            print("Registration Successful")
    allLogin = Login.query.all()
    print(allLogin)
    return render_template("home.html")

# Route for login page
@app.route('/log', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = Login.query.filter_by(email=email, password=password).first()
        if user:
            flash("Login Successful", "success")
            print("Login Successful")
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password", "danger")
            print("Invalid email or password")
            return redirect('/log')
    return render_template("log.html")

# Route to save movie data
@app.route('/https://imdb236.p.rapidapi.com/imdb/save_movie', methods=['POST'])
def save_movie():
    movie_data = request.json

    # Store the search term in the database
    movie_title = movie_data.get('Title')
    print(movie_title)  # Print the movie data to the console
    search = Search(movie=movie_title)
    db.session.add(search)
    db.session.commit()

    return jsonify({"message": "Movie data saved successfully"}), 200

# Route for search history
@app.route('/history', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        movie = request.form['movie']
        search = Search(movie=movie)
        db.session.add(search)
        db.session.commit()
        flash("Search Successful", "success")
        print("Search Successful")

    allSearch = Search.query.all()
    print(allSearch)
    return render_template("history.html", allSearch=allSearch)

# Route for show page
@app.route('/show')
def show():
    return "This is show page"

# Route for index page
@app.route('/')
def index():
    return render_template("index.html")

# Route to delete a search record
@app.route('/history/delete/<int:sno>')
def delete(sno):
    search = Search.query.filter_by(sno=sno).first()
    db.session.delete(search)
    db.session.commit()
    flash("Record deleted successfully", "success")
    return redirect("/history")

if __name__ == "__main__":
    app.run(debug=True)