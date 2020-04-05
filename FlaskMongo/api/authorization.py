from flask import request
from flask import jsonify
from flask_restful import Resource
from MongoEngineDB.Models.Users import User


class SignUpApi(Resource):
    def post(self):
        data = request.get_json()
        post_user = User(**data)
        post_user.generate_pw_hash()
        post_user.save()
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})