from flask import Flask, render_template, redirect, url_for, abort
from flask_bootstrap import Bootstrap
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from functools import wraps
import stripe
from forms import CreateNewUser, Login, NewItem, Search

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config[
    'STRIPE_PUBLIC_KEY'] = 'pk_test_51KitWqIAGZLPKTsnfeLBAjUfyCKqpdKy5RUp9DzzGSb1dbrteXcXa4K3hbIU5ImehIlQL7pVxPYNzFWXzhgNnkdm00etiS6jOG'
app.config[
    'STRIPE_SECRET_KEY'] = 'sk_test_51KitWqIAGZLPKTsnkZzbp7U7oJ3dr8NKJ7JQprGHQfDxIvoa8yWG1OWXGOZr6fFxBZO8D5LvcGj8NgjLzLVCR1T400dgBYC4jw'
YOUR_DOMAIN = 'http://127.0.0.1:5000'
stripe.api_key = app.config['STRIPE_SECRET_KEY']
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online-shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(250), nullable=False)


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def admin_only(f):
    @wraps(f)
    def dec_func(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)

    return dec_func


@app.route('/', methods=['GET', 'POST'])
def home():
    goods = Goods.query.all()
    form = Search()
    if form.validate_on_submit():
        goods = Goods.query.filter(Goods.name.like(f"%{form.search.data}%")).all()
    return render_template('index.html', goods=goods, form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = CreateNewUser()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        check_user = User.query.filter_by(email=email).first()
        if check_user:
            error = "You've already signed up with that email, log in instead!"
            form = Login()
            return render_template('login.html', form=form, error=error)

        new_user = User(
            name=name,
            email=email,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    form = Login()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                error = 'Incorrect password!'
        else:
            error = "This email doesn't exist!"

    return render_template('login.html', form=form, error=error)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
@admin_only
def add():
    form = NewItem()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        price = float(form.price.data)
        img_url = form.img_url.data
        new_item = Goods(
            name=name,
            description=description,
            price=price,
            img_url=img_url,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_item)
        db.session.commit()
        stripe.Product.create(id=new_item.id, name=name, description=description, images=[img_url])
        stripe.Price.create(unit_amount=int(str(price).replace('.', '')), currency='USD', product=new_item.id,
                            metadata={'id': f'{new_item.id}'})
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/payment/<int:id>', methods=['POST'])
def payment(id):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    try:
        ids = list(reversed(stripe.Price.list()['data']))
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': f'{ids[id]["id"]}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for('home', _external=True),
            cancel_url=url_for('home', _external=True),
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@app.route('/delete/<int:id>')
@admin_only
def delete(id):
    selected_item = Goods.query.get(id)
    db.session.delete(selected_item)
    db.session.commit()
    stripe.Product.delete(str(id))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
