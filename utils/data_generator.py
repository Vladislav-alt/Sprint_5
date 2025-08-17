import random
import string


def generate_email(prefix_length=8, domain="example.com"):
    """Генерация email (логина)"""
    letters = string.ascii_lowercase + string.digits
    prefix = "".join(random.choice(letters) for _ in range(prefix_length))
    return f"{prefix}@{domain}"


def generate_password(length=10):
    """Генерация пароля"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))
