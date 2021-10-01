from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

CORRECT_API_KEY = 'AdeleIsTheBest'

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    cafes_list = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafes_list)


@app.route('/search')
def find_cafe():
    location = request.args.get('loc').title()
    cafes = db.session.query(Cafe).filter(Cafe.location == location)
    cafes_list = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafes_list) if cafes_list else jsonify(error={"Not found": "Sorry, we don't have a cafe at that location"})


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_wifi=bool(request.form.get('has_wifi')),
        has_toilet=bool(request.form.get('has_toilet')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new cafe.'})


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    selected_cafe = Cafe.query.get(cafe_id)
    if selected_cafe:
        selected_cafe.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(success='Successfully updated the price.'), 200
    return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database.'}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api_key')
    if api_key == CORRECT_API_KEY:
        selected_cafe = Cafe.query.get(cafe_id)
        if selected_cafe:
            db.session.delete(selected_cafe)
            db.session.commit()
            return jsonify(success='Successfully deleted the cafe.'), 200
        return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database.'}), 404
    return jsonify(error='Sorry, you are not allowed to delete a cafe. Make sure you have the correct api_key.'), 403


if __name__ == '__main__':
    app.run(debug=True)
