"""generate totp"""
import pyotp
import hashlib
from base64 import b32encode


def generate_totp(secret):
    # Hash the email to create a secret key
    # hash = hashlib.sha256(email.encode()).digest()
    # # convert it into base 32
    # secret_key = b32encode(hash).decode()
    # print(secret_key)

    # Create a TOTP object
    totp = pyotp.TOTP(secret, interval=30)

    # Generate the current TOTP
    current_totp = totp.now()

    return current_totp


# Example usage:
def totp_helper(secret: str):
    # Replace 'user@example.com' with the actual email
    # email = 'user@example.com'

    # Generate TOTP based on the email
    totp_code = generate_totp(secret)

# totp_helper("muhammad@gmail.com")