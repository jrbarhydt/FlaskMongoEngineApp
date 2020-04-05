# flask packages
from flask import jsonify
from flask import request
from flask import Blueprint
# mongo-engine classes
from MongoEngineDB.Models.Reservations import Reservation


reservation = Blueprint('reservation', __name__, url_prefix='/reservation')


# /reservation
@reservation.route('/', methods=['GET'])
def get_all_reservations():
    output = Reservation.objects()
    return jsonify({'result': output})


@reservation.route('/<reservation_id>', methods=['GET'])
def get_one_reservation(reservation_id):
    return jsonify({'result': Reservation.objects(id=reservation_id)})


@reservation.route('/', methods=['POST'])
def add_reservation():
    data = request.get_json()
    res = Reservation(**data).save()
    output = {'id': str(res.id)}
    return jsonify({'result': output})


@reservation.route('/<reservation_id>', methods=['PUT'])
def modify_reservation(reservation_id):
    data = request.get_json()
    res = Reservation.objects(id=reservation_id).update(**data)
    return jsonify({'result': res})


@reservation.route('/<reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    return jsonify({'result': Reservation.objects(id=reservation_id).delete()})
