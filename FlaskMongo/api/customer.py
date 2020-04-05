# flask packages
from flask import jsonify
from flask import request
from flask import Blueprint
from flask_restful import Resource
# mongo-engine classes
from MongoEngineDB.Models.Customers import Customer


class CustomersApi(Resource):
    def get(self):
        output = Customer.objects()
        return jsonify({'result': output})

    def post(self):
        data = request.get_json()
        post_customer = Customer(**data).save()
        output = {'id': str(post_customer.id)}
        return jsonify({'result': output})


class CustomerApi(Resource):
    def get(self, customer_id):
        jsonify({'result': Customer.objects(id=customer_id)})

    def put(self, customer_id):
        data = request.get_json()
        put_customer = Customer.objects(id=customer_id).update(**data)
        return jsonify({'result': put_customer})

    def delete(self, customer_id):
        return jsonify({'result': Customer.objects(id=customer_id).delete()})


class RandomCustomersApi(Resource):
    def get(self, quantity):
        return jsonify({'result': [item for item in Customer.get_random_customer(int(quantity))]})
