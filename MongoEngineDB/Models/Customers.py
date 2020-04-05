from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, ListField, StringField, \
    EmailField, DateField, ReferenceField
from MongoEngineDB.Models.Dishes import Dish
from MongoEngineDB.Tools.RandomMongoEngineObject import get_random
import re


class AddressField(EmbeddedDocument):
    street = StringField()
    city = StringField()
    state = StringField()


class PhoneField(StringField):
    # Modification of http://regexlib.com/REDetails.aspx?regexp_id=61
    #
    # US Phone number that accept a dot, a space, a dash, a forward slash, between the numbers.
    # Will Accept a 1 or 0 in front. Area Code not necessary
    REGEX = re.compile(r"((\(\d{3}\)?)|(\d{3}))([-\s./]?)(\d{3})([-\s./]?)(\d{4})")

    def validate(self, value):
        if not PhoneField.REGEX.match(value):
            self.error(f"ERROR: `{value}` Is An Invalid Phone Number.")
        super(PhoneField, self).validate(value=value)


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
