from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm, MovieForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['UPLOAD_FOLDER'] = "static/uploads"

db = SQLAlchemy(app)

from models import User, Movie


@app.route('/')
def home():
    return redirect(url_for('login'))


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password", "danger")

    return render_template('login.html', form=form)


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pw)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    movies = Movie.query.all()
    return render_template('dashboard.html', movies=movies)


# ---------------- ADD MOVIE ----------------
@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        file = form.poster.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        movie = Movie(
            title=form.title.data,
            description=form.description.data,
            rating=form.rating.data,
            poster=filename
        )

        db.session.add(movie)
        db.session.commit()

        flash("Movie added!", "success")
        return redirect(url_for('dashboard'))

    return render_template('add_movie.html', form=form)


# ---------------- MOVIE DETAILS ----------------
@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie_details.html', movie=movie)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
