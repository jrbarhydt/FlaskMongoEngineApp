# flask packages
from flask import jsonify
from flask import request
from flask import Blueprint
# mongo-engine classes
from MongoEngineDB.Models.Dishes import Dish


dish = Blueprint('dish', __name__, url_prefix='/dish')


# /dish
@dish.route('/', methods=['GET'])
def get_all_dishes():
    output = Dish.objects()
    return jsonify({'result': output})


@dish.route('/<dish_id>', methods=['GET'])
def get_one_dish(dish_id):
    return jsonify({'result': Dish.objects(id=dish_id)})


@dish.route('/rnd/<int:qty>', methods=['GET'])
def get_random_dish(qty):
    return jsonify({'result': [item for item in Dish.get_random_dish(int(qty))]})


@dish.route('/', methods=['POST'])
def add_dish():
    data = request.get_json()
    post_dish = Dish(**data).save()
    output = {'id': str(post_dish.id)}
    return jsonify({'result': output})


@dish.route('/<dish_id>', methods=['PUT'])
def modify_dish(dish_id):
    data = request.get_json()
    put_dish = Dish.objects(id=dish_id).update(**data)
    return jsonify({'result': put_dish})


@dish.route('/<dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    return jsonify({'result': Dish.objects(id=dish_id).delete()})