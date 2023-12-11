"""send totp to client on his mail"""
import smtplib
from os import environ


def template(name: str, otp,):
    with open("template.txt", "r") as file:
        email_template = file.read()

    message = email_template.replace("[user]", name)
    message = message.replace("[otp]", otp)
    print(message)
    return message


def send_mail(send_to: str, name: str, otp):
    message = template(name, otp)
    my_email = environ.get("FROM")
    my_password = environ.get("APP_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com") as email_conn:
        email_conn.starttls()
        email_conn.login(user=my_email, password=my_password)
        email_conn.sendmail(from_addr=my_email, to_addrs=send_to, msg=message)


def mail_helper(send_to: str, otp):
    name = send_to.split("@")[0]
    send_mail(send_to, name, otp)
