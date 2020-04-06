# flask packages
from flask import jsonify
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
# mongo-engine classes
from MongoEngineDB.Models.Users import User


class UsersApi(Resource):
    @jwt_required
    def get(self):
        output = User.objects()
        return jsonify({'result': output})

    def post(self):
        data = request.get_json()
        post_user = User(**data).save()
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})


class UserApi(Resource):
    @jwt_required
    def get(self, user_id):
        print(f"JWT ID: {get_jwt_identity()}")
        return jsonify({'result': User.objects.get(id=user_id)})

    @jwt_required
    def put(self, user_id):
        data = request.get_json()
        put_user = User.objects(id=user_id).update(**data)
        return jsonify({'result': put_user})

    @jwt_required
    def delete(self, user_id):
        return jsonify({'result': User.objects(id=user_id).delete()})

