from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, email


class CreateNewUser(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign up")


class Login(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class NewItem(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Add")


class Search(FlaskForm):
    search = StringField("", validators=[DataRequired()])
    submit = SubmitField("Search")
