from app import app
from flask import request
from app import db
from Dishes import Dishes

@app.route('/')
def index():
    firstmember = Dishes.query.first()
    return '<h1> Here you can find dishes list! </h1>'

@app.route('/dishes')
def view():
    dishes = Dishes.query.first()
    if dishes is not None:
        return str('First member name \n' + dishes.__str__())
    else:
        return "Dishes with this id does not exist"

@app.route('/dishes/<id>')
def get_dishes(id):
    dishes = Dishes.query.get(id)
    if dishes is not None:
        return dishes.__str__()
    else:
        return "Dishes with this id does not exist"

@app.route('/dishes', methods=['POST'])
def add_dishes():
    dishes_id = request.json['id']
    price = request.json['price']
    material = request.json['material']
    color = request.json['color']

    new_dishes = Dishes()
    new_dishes.dishes_id = dishes_id
    new_dishes.dishes_price = price
    new_dishes.dishes_material = material
    new_dishes.dishes_color = color

    db.session.add(new_dishes)
    db.session.commit()

    return str(new_dishes.__str__())

@app.route('/dishes/<id>', methods=['PUT'])
def dishes_update(id):
    price = request.json['price']
    material = request.json['material']
    color = request.json['color']

    new_dishes = Dishes.query.get(id)
    new_dishes.dishes_id = id
    new_dishes.dishes_price = price
    new_dishes.dishes_material = material
    new_dishes.dishes_color = color

    db.session.commit()

    return new_dishes.__str__()

@app.route('/dishes/<id>', methods=['DELETE'])
def dishes_delete(id):
    dishes = Dishes.query.get(id)
    db.session.delete(dishes)
    db.session.commit()

    return str("Deleting succssesful")