import mongoengine
from MongoEngineDB.Tools.CsvToMongoEngine import (tab_separated_to_dish,
                                                  tab_separated_to_reservation,
                                                  tab_separated_to_order,
                                                  tab_separated_to_customer)

client = mongoengine.connect("test")
# tab_separated_to_dish(filename="../Resources/dishes")
# tab_separated_to_customer(filename="../Resources/customers")
# tab_separated_to_order(filename="../Resources/orders")
#
tab_separated_to_reservation(filename="../Resources/reservations")