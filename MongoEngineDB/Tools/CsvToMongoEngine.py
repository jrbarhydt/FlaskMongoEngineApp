from MongoEngineDB.Models.Dishes import Dish
from MongoEngineDB.Models.Customers import Customer, AddressField
from MongoEngineDB.Models.Orders import Order
from MongoEngineDB.Models.Reservations import Reservation
from mongoengine.errors import ValidationError
import random


def tab_separated_to_dish(filename="../Resources/dishes"):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            try:
                data = line.split('\t')
                price = float(data.pop())
                desc = data.pop()
                name = data.pop()

                dish = Dish(name=name, description=desc, price=price).save()
                print(f"Added: {dish.name} | {dish.description} | {dish.price} => {dish.id}")
            except ValueError:
                print(f"Invalid Entry: {line}")


def tab_separated_to_customer(filename="../Resources/customers"):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            try:
                data = line.split('\t')
                favorite_dishes = data.pop()
                favorite_dishes = Dish.get_random_dish()
                birthday = data.pop()
                phone = data.pop()
                address_state = data.pop()
                address_city = data.pop()
                address_street = data.pop()
                email = data.pop()
                last_name = data.pop()
                first_name = data.pop()

                user = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                birthday=birthday,
                                favorite_dishes=favorite_dishes)
                user.address = AddressField(street=address_street, city=address_city, state=address_state)
                user.save()
                print(f"Added: "
                      f"{user.first_name} | "
                      f"{user.last_name} | "
                      f"{user.email} | "
                      f"{user.phone} | "
                      f"{user.birthday} | "
                      f"{user.favorite_dishes} | "
                      f"{user.address.street} | "
                      f"{user.address.city} | "
                      f"{user.address.state} => {user.id}")
            except ValueError:
                print(f"Invalid Entry: {line}")
            except ValidationError:
                print(f"Invalid Entry: {line}")
            # except KeyError:
            #     print(f"Line Not Added (Is it the first line?) => {line}")


def tab_separated_to_order(filename="../Resources/orders"):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            try:
                data = line.split('\t')
                time = data.pop()
                items = Dish.get_random_dish(random.randint(0, 5))
                customer = Customer.get_random_customer().pop()

                order = Order(time=time, customer=customer, items=items)
                order.save()
                print(f"Added: {order.time} | {order.customer} | {order.items} => {order.id}")
            except ValueError:
                print(f"Invalid Entry: {line}")
            except ValidationError:
                print(f"Invalid Entry: {line}")
            except KeyError:
                print(f"Line Not Added (Is it the first line?) => {line}")


def tab_separated_to_reservation(filename="../Resources/reservations"):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            try:
                data = line.split('\t')
                party_size = data.pop()
                time = data.pop()
                items = Dish.get_random_dish(random.randint(0, 5))
                customer = Customer.get_random_customer().pop()

                reservation = Reservation(time=time, customer=customer, party_size=party_size, items=items)
                reservation.save()
                print(f"Added: {reservation.time} | {reservation.customer} | {party_size} | {reservation.items} => "
                      f"{reservation.id}")
            except ValueError:
                print(f"Invalid Entry: {line}")
            except ValidationError:
                print(f"Invalid Entry: {line}")