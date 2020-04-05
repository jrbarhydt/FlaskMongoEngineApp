from mongoengine import Document, StringField, FloatField
from MongoEngineDB.Tools.RandomMongoEngineObject import get_random


class Dish(Document):
    name = StringField(required=True)
    description = StringField()
    price = FloatField()
    image_url = StringField()

    @staticmethod
    def get_random_dish(quantity=1):
        return get_random(Dish, quantity)
