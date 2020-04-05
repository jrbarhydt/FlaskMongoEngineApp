from flask import request
from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from MongoEngineDB.Models.Users import User
from FlaskMongo.api.error import invalid_login
import datetime


class SignUpApi(Resource):
    def post(self):
        data = request.get_json()
        post_user = User(**data)
        post_user.generate_pw_hash()
        post_user.save()
        output = {'id': str(post_user.id)}
        return jsonify({'result': output})


class LoginApi(Resource):
    def post(self):
        data = request.get_json()
        user = User.objects.get(email=data.get('email'))
        auth_success = user.check_pw_hash(data.get('password'))
        if not auth_success:
            return invalid_login()
        else:
            expiry = datetime.timedelta(days=5)
            jwt = create_access_token(identity=str(user.id), expires_delta=expiry)
            return jsonify({'result': {'token': jwt, 'logged_in_as': f"{user.email}"}})
