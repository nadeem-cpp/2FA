# todo for the 1st time start, the user must choose configuration
# todo 1 let the user choose from 2 settings, mail verification or authenticator app
# todo we will manage a user database to choose if user is registered for mail or authentication
# todo 2 if user choose mail generate totp code and mail it, return that code in respone to calling application so it can verify the code
# todo 2 if user choose authenticator app, share a QRCode that will share a secret key with the authenticator
# todo 3 user will share the key and confirm its authenticity
# todo 4 user can request new key in mail method
# todo since it is a time based, so after 30 seconds key will expire
import sys
from os import environ
from mail.mail import mail_helper


def email_method_init():
    application = input("enter the company name\n")
    sender_mail = input("enter the company gmail\n")
    environ["FROM"] = sender_mail
    email_template = f"""Subject: {application} Two-Factor Authentication Code

Dear [user],

To enhance the security of your {application} account, please use the following One-Time Password (OTP) for authentication:

Your OTP: [otp]

This code is valid for the next [time duration]. If you did not attempt to log in, please secure your account and contact us.

Thank you for choosing {application}.

Best regards,

{application}
Contact Us at: {sender_mail}
"""
    # save the template at mail/template.txt
    with open("mail/template.txt", "w") as file:
        file.write(email_template)

    # gmail authenticator passcode
    # enable 2 factors authentication on gmail then create app password and paste it here
    # replace it with app documentation link
    app_password_guide = "https://support.google.com/accounts/answer/185833?hl=en"
    environ["APP_PASSWORD"] = input(
        f"Enter Gmail APP password.\nFor guide on how to create one\nClick here:{app_password_guide}\n")
    # save secrets in db/ or save it in aws secret managers for security / or env variables


def google_method_init():
    pass


def init_function():
    init_required: bool = True
    while init_required:
        print("Choose between mail authentication or Google Authentication")
        choice = input("Enter 1 for mail;\n2 for Google authentication;\n")
        if choice == "1":
            environ["METHOD"] = "mail"
            email_method_init()
            init_required = False
        elif choice == "2":
            environ["METHOD"] = "auth"
            google_method_init()
            init_required = False
        else:
            print("Kindly choose between 1 and 2")


def run_function(mail: str):
    # if mail is true, send otp to mail
    if environ.get("METHOD") is None:
        print("Please first init the program")
    else:
        if environ.get("METHOD") == "mail":
            mail_helper(send_to=mail)
    # if google auth is true, generate otp from secret key and send it to app, so it can verify
    # Placeholder for another function
    print("Another function executed.")


def main():
    # Check if a command is provided
    if len(sys.argv) < 2:
        print("Usage: python main.py [command]\n command: init,\trun")
        sys.exit(1)

    # Extract the command from the command line arguments
    command = sys.argv[1]

    # Perform actions based on the provided command
    if command == 'init':
        init_function()
    elif command == 'run':
        try:
            email = sys.argv[2]
            run_function(email)
        except IndexError:
            print("Please enter email in command.\nExample: py main.py run demo@gmail.com")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
