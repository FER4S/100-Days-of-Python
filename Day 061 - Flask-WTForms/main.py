from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired(), validators.length(min=8)])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.secret_key = 'xdxdxdxd'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
