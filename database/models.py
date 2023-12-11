from .db import db
import hashlib
from base64 import b32encode


class User(db.Model):
    email = db.Column(db.String(20), primary_key=True)
    secret = db.Column(db.String(32), unique=True, nullable=False)

    @classmethod
    def get_or_generate_secret(cls, email) -> str:
        try:
            user = cls.objects.get(mail=email)
            return user.secret
        except cls.DoesNotExist:
            secret = cls.generate_secret(email=email)
            user = cls(mail=email, secret=secret)
            user.save()
            return secret

    @classmethod
    def generate_secret(cls, email) -> str:
        # Hash the email to create a secret key
        secret = hashlib.sha256(email.encode()).digest()
        # convert it into base 32
        secret_key = b32encode(secret).decode()
        print(secret_key)
        return secret_key



