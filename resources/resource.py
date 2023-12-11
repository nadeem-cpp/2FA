from database.models import User
from flask import request, jsonify, session
from flask_restful import Resource
from resources.otp.totp import generate_totp


class Otp(Resource):
    def post(self):
        """"Take email and send OTP to that email"""
        try:
            data = request.get_json()
            mail = data.get("mail")
            session["mail"] = mail
            user_secret = User.get_or_generate_secret(email=mail)
            print(f"user secret is {user_secret}")
            otp = generate_totp(user_secret)
            print(f"otp is {otp}")
            session["otp"] = otp
            # mail_helper(mail, otp)
            return jsonify({
                "code": 200,
                "msg": "OTP sent via email!"
                })
        except Exception as e:
            return jsonify({
                "error": str(e),
                "code": 500,
            })


class Authentication(Resource):

    def post(self):
        """"Take user entered OTP from JSON body and match it with the real OTP"""
        try:
            data = request.get_json()
            entered_otp = data.get("otp")
            mail = session.get("mail")
            if mail is None:
                return jsonify({
                    "code": 500,
                    "msg": "Mail not found"
                })
            else:
                otp = session.get("otp")
                if otp == entered_otp:
                    return jsonify({
                        "code": 200,
                        "msg": "OTP matched"
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


