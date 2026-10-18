import hashlib
import os

users_db = {}

def hash_password(password: str, salt: bytes = None):
    salt = salt or os.urandom(16)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return salt, hashed

def register_user(email: str, password: str) -> bool:
    if not email or "@" not in email:
        raise ValueError("Invalid email")
    if len(password) < 8:
        raise ValueError("Password too short")
    if email in users_db:
        return False
    salt, hashed = hash_password(password)
    users_db[email] = {"salt": salt, "hash": hashed, "verified": False}
    return True

def verify_email(email: str) -> bool:
    if email in users_db:
        users_db[email]["verified"] = True
        return True
    return False