from mongoengine import Document, ListField, ReferenceField, DateTimeField
from MongoEngineDB.Models.Dishes import Dish
from MongoEngineDB.Models.Customers import Customer
from MongoEngineDB.Tools.RandomMongoEngineObject import get_random


class Order(Document):
    time = DateTimeField()
    items = ListField(ReferenceField(Dish))
    customer = ReferenceField(Customer)

    @staticmethod
    def get_random_order(quantity=1):
        return get_random(Order, quantity)