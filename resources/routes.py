from .resource import Authentication, Otp


def init_routes(api):
    api.add_resource(Authentication, "/authenticate")
    api.add_resource(Otp, "/generate_otp")

