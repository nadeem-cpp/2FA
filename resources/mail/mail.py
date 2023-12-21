"""send totp to client on his mail"""
import smtplib
from os import environ, path

MY_EMAIL = environ.get("FROM")
APP_PASSWORD = environ.get("APP_PASSWORD")

template_path = path.abspath("resources/mail/template.txt")


def template(name: str, otp,):
    with open(template_path, "r") as file:
        email_template = file.read()

    message = email_template.replace("[user]", name)
    message = message.replace("[otp]", otp)
    print(message)
    return message


def send_mail(send_to: str, name: str, otp):
    message = template(name, otp)
    with smtplib.SMTP("smtp.gmail.com") as email_conn:
        email_conn.starttls()
        email_conn.login(user=MY_EMAIL, password=APP_PASSWORD)
        email_conn.sendmail(from_addr=MY_EMAIL, to_addrs=send_to, msg=message)


def mail_helper(send_to: str, otp):
    name = send_to.split("@")[0]
    send_mail(send_to, name, otp)
