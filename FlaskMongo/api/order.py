# flask packages
from flask import jsonify
from flask import request
from flask import Blueprint
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
# mongo-engine classes
from MongoEngineDB.Models.Orders import Order
from MongoEngineDB.Models.Users import User

order = Blueprint('order', __name__, url_prefix='/order')


class OrdersApi(Resource):
    def get(self):
        return jsonify({'result': Order.objects()})


# /order
# @order.route('/', methods=['GET'])
# def get_all_orders():
#     output = Order.objects()
#     return jsonify({'result': output})


@order.route('/<order_id>', methods=['GET'])
def get_one_order(order_id):
    return jsonify({'result': Order.objects(id=order_id)})


@order.route('/', methods=['POST'])
@jwt_required
def add_order():
    authorized_user = User.objects(id=get_jwt_identity(), access__server=True)
    if authorized_user:
        data = request.get_json()
        post_order = Order(**data).save()
        output = {'id': str(post_order.id)}
        return jsonify({'result': output})
    else:
        return jsonify({"message": "Unauthorized User"})

@order.route('/<order_id>', methods=['PUT'])
def modify_order(order_id):
    data = request.get_json()
    put_order = Order.objects(id=order_id).update(**data)
    return jsonify({'result': put_order})


@order.route('/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    return jsonify({'result': Order.objects(id=order_id).delete()})
