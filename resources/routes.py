from .resource import UserAuthentication


def init_routes(api):
    api.add_resource(UserAuthentication, "/user/auth")

