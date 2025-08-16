import random
import string

def generate_email():
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = random.choice(["yandex.ru", "mail.ru", "gmail.com"])
    return f"{name}@{domain}"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))