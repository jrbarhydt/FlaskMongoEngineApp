from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, ListField, StringField, \
    EmailField, DateField, ReferenceField
from MongoEngineDB.Models.Dishes import Dish
from MongoEngineDB.Tools.RandomMongoEngineObject import get_random
from MongoEngineDB.Models.Users import PhoneField


class AddressField(EmbeddedDocument):
    street = StringField()
    city = StringField()
    state = StringField()


class Customer(Document):
    first_name = StringField(required=True)
    last_name = StringField()
    email = EmailField()
    address = EmbeddedDocumentField(AddressField)
    phone = PhoneField()
    birthday = DateField()
    favorite_dishes = ListField(ReferenceField(Dish))

    @staticmethod
    def get_random_customer(quantity=1):
        return get_random(Customer, quantity)
