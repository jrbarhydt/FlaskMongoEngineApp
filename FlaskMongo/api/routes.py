from .customer import CustomerApi, CustomersApi, RandomCustomersApi


def create_route(api):
    api.add_resource(CustomersApi, '/customer/')
    api.add_resource(CustomerApi, '/customer/<customer_id>')
    api.add_resource(RandomCustomersApi, '/customer/rnd/<quantity>')
