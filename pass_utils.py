from hashlib import scrypt
from os import urandom
from base64 import b64encode, b64decode
from hmac import compare_digest

def create_password(password: str) -> str:
    salt = urandom(16)
    key = scrypt(
        password.encode(),
        salt=salt,
        n=16384,
        r=8,
        p=1
    )
    return b64encode(salt + key).decode()


def verify_password(stored_password: str, password_input: str) -> bool:
    data = b64decode(stored_password.encode())
    salt = data[:16]
    stored_key = data[16:]

    new_key = scrypt(
        password_input.encode(),
        salt=salt,
        n=16384,
        r=8,
        p=1
    )

    return compare_digest(new_key, stored_key)