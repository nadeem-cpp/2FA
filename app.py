from flask import Flask, render_template, session, redirect, url_for
from database import db
from flask_restful import Api
from database.models import User
# from flask_session import Session
from resources import routes
from totp import generate_totp
from mail.mail import mail_helper

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.secret_key = "kahga/a;r4rra12"
# Session(app)
db.init_db(app)
api = Api(app)
routes.init_routes(api)


@app.route('/')
def index():
    return "this is a 2FA application running on flask"


@app.route('/auth/email/<string:mail>')
def admin(mail):
    user_secret = User.get_or_generate_secret(email=mail)
    print(f"user secret is {user_secret}")
    otp = generate_totp(user_secret)
    mail_helper(mail, otp)
    return render_template("auth.html")


if __name__ == '__main__':
    app.run()
