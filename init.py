from os import environ


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
    with open("resources/mail/template.txt", "w") as file:
        file.write(email_template)

    # gmail authenticator passcode
    # enable 2 factors authentication on gmail then create app password and paste it here
    # replace it with app documentation link
    app_password_guide = "https://support.google.com/accounts/answer/185833?hl=en"
    environ["APP_PASSWORD"] = input(
        f"Enter Gmail APP password.\nFor guide on how to create one\nClick here:{app_password_guide}\n")
    # save secrets in db/ or save it in aws secret managers for security / or env variables

    print("Congratulations\nYou App setup is completed, You can noe run the app")


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
            print("Incoming")
            # google_method_init()
            # init_required = False
        else:
            print("Kindly choose between 1 and 2")


if __name__ == "__main__":
    init_function()
