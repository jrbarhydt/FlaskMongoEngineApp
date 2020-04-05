# flask packages
from flask import Flask
from flask import jsonify
from flask import request
from flask_mongoengine import MongoEngine
# mongo-engine classes
from MongoEngineDB.Models.Customers import Customer
from MongoEngineDB.Models.Orders import Order
from MongoEngineDB.Models.Reservations import Reservation
# blueprints
from FlaskMongo.api.dish import dish
from FlaskMongo.api.customer import customer
from FlaskMongo.api.reservation import reservation
# error handler
from FlaskMongo.api.error import invalid_route

# init flask and mongo-engine
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/test_database'}
app.register_blueprint(dish)
app.register_blueprint(customer)
app.register_blueprint(reservation)
db = MongoEngine()
db.init_app(app)


@app.errorhandler(404)
def err(e):
    return invalid_route(e)

