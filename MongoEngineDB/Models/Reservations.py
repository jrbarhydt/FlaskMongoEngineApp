from mongoengine import Document, ListField, ReferenceField, DateTimeField, IntField
from MongoEngineDB.Models.Dishes import Dish
from MongoEngineDB.Models.Customers import Customer
from MongoEngineDB.Tools.RandomMongoEngineObject import get_random


class Reservation(Document):
    time = DateTimeField()
    items = ListField(ReferenceField(Dish))
    customer = ReferenceField(Customer)
    party_size = IntField()

    @staticmethod
    def get_random_reservation(quantity=1):
        return get_random(Reservation, quantity)
