from .customer import CustomerApi, CustomersApi, RandomCustomersApi
from .authentication import SignUpApi, LoginApi
from .user import UserApi, UsersApi
from .order import OrdersApi
# from .reset_password import ForgotPassword, ResetPassword


def create_routes(api):
    api.add_resource(CustomersApi, '/customer/')
    api.add_resource(CustomerApi, '/customer/<customer_id>')
    api.add_resource(RandomCustomersApi, '/customer/rnd/<quantity>')

    api.add_resource(SignUpApi, '/authentication/signup')
    api.add_resource(LoginApi, '/authentication/login')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(OrdersApi, '/order/')
    # api.add_resource(ResetPassword, '/authentication/reset')
    # api.add_resource(ForgotPassword, '/authentication/forgot')
