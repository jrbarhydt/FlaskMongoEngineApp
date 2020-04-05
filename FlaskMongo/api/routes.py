from .customer import CustomerApi, CustomersApi, RandomCustomersApi
from .authorization import SignUpApi


def create_routes(api):
    api.add_resource(CustomersApi, '/customer/')
    api.add_resource(CustomerApi, '/customer/<customer_id>')
    api.add_resource(RandomCustomersApi, '/customer/rnd/<quantity>')

    api.add_resource(SignUpApi, '/authorization/signup')