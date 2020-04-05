# flask packages
from flask import jsonify
from flask import request
from flask import Blueprint
# mongo-engine classes
from MongoEngineDB.Models.Customers import Customer


customer = Blueprint('customer', __name__, url_prefix='/customer')


# /customer
@customer.route('', methods=['GET'])
def get_all_customers():
    output = Customer.objects()
    return jsonify({'result': output})


@customer.route('/<customer_id>', methods=['GET'])
def get_one_customer(customer_id):
    return jsonify({'result': Customer.objects(id=customer_id)})


@customer.route('/rnd/<int:qty>', methods=['GET'])
def get_random_customer(qty):
    return jsonify({'result': [item for item in Customer.get_random_customer(int(qty))]})


@customer.route('', methods=['POST'])
def add_customer():
    data = request.get_json()
    post_customer = Customer(**data).save()
    output = {'id': str(post_customer.id)}
    return jsonify({'result': output})


@customer.route('/<customer_id>', methods=['PUT'])
def modify_customer(customer_id):
    data = request.get_json()
    put_customer = Customer.objects(id=customer_id).update(**data)
    return jsonify({'result': put_customer})


@customer.route('/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    return jsonify({'result': Customer.objects(id=customer_id).delete()})