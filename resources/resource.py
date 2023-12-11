from database.models import User
from flask import request, jsonify, session
from flask_restful import Resource
from mail.mail import mail_helper


class UserAuthentication(Resource):
    def post(self):
        try:
            data = request.get_json()
            print(data)
            user = User.objects(**data)
            if len(user) > 0:
                session["admin"] = True
                return jsonify({
                    "code": 200,
                })
            else:
                return jsonify({
                    "code": 300,
                })
        except Exception as e:
            return jsonify({
                "error": str(e),
                "code": 500,
            })
