from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length


# ----------------------------
# Registration Form
# ----------------------------
class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=20)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")]
    )

    submit = SubmitField("Register")


# ----------------------------
# Login Form
# ----------------------------
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


# ----------------------------
# Add Movie Form
# ----------------------------
class AddMovieForm(FlaskForm):
    title = StringField(
        "Movie Title",
        validators=[DataRequired()]
    )

    description = TextAreaField(
        "Movie Description",
        validators=[DataRequired(), Length(min=10)]
    )

    poster_url = StringField(
        "Poster Image URL",
        validators=[DataRequired()]
    )

    rating = IntegerField(
        "Rating (1–10)",
        validators=[DataRequired()]
    )

    submit = SubmitField("Add Movie")


# ----------------------------
# Edit Movie Form
# ----------------------------
class EditMovieForm(FlaskForm):
    title = StringField(
        "Movie Title",
        validators=[DataRequired()]
    )

    description = TextAreaField(
        "Movie Description",
        validators=[DataRequired(), Length(min=10)]
    )

    poster_url = StringField(
        "Poster Image URL",
        validators=[DataRequired()]
    )

    rating = IntegerField(
        "Rating (1–10)",
        validators=[DataRequired()]
    )

    submit = SubmitField("Update Movie")
