# Тестовые пользователи
VALID_USER = {
    "email": "vladpotapov28111@yandex.ru",
    "password": "qwerty",
    "name": "Владимир"
}

INVALID_USERS = [
    {"email": "invalid-email", "password": "123456"},  # Неправильный email
    {"email": "test@test.ru", "password": "123"},      # Слишком короткий пароль
    {"email": "", "password": "123456"},               # Пустой email
]

