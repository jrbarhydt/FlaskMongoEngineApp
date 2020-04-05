# flask packages
from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
# blueprints
from FlaskMongo.api.dish import dish
from FlaskMongo.api.reservation import reservation
# error handler
from FlaskMongo.api.error import invalid_route
# api routes
from FlaskMongo.api.routes import create_routes

# init flask, flask-restful, flask-bcrypt, flask-mongo-engine, and flask-jwt-extended
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/test_database'}
app.config.from_envvar('ENV_FILE_LOCATION')
app.register_blueprint(dish)
app.register_blueprint(reservation)

b_crypt = Bcrypt(app)
api = Api(app=app)
db = MongoEngine(app=app)
jwt = JWTManager(app=app)

# init api routes
create_routes(api=api)


@app.errorhandler(404)
def err(e):
    return invalid_route(e)

