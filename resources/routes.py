from .resource import Authentication, Otp


def init_routes(api):
    api.add_resource(Authentication, "/user/auth")
    api.add_resource(Otp, "/sendotp")

