# flask packages
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
# blueprints
from FlaskMongo.api.dish import dish
from FlaskMongo.api.reservation import reservation
# error handler
from FlaskMongo.api.error import invalid_route
# api routes
from FlaskMongo.api.routes import create_route
# init flask, flask-restful, and flask-mongo-engine
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/test_database'}
app.register_blueprint(dish)
app.register_blueprint(reservation)

api = Api(app=app)
db = MongoEngine(app=app)

# init api routes
create_route(api=api)


@app.errorhandler(404)
def err(e):
    return invalid_route(e)

