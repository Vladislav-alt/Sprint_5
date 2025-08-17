class Urls:
    """Класс для хранения всех URL проекта"""
    BASE = "https://stellarburgers.nomoreparties.site"
    
    # Основные страницы
    MAIN = BASE
    LOGIN = f"{BASE}/login"
    REGISTER = f"{BASE}/register"
    FORGOT_PASSWORD = f"{BASE}/forgot-password"
    RESET_PASSWORD = f"{BASE}/reset-password"
    
    # Личный кабинет
    PROFILE = f"{BASE}/account/profile"
    ORDER_HISTORY = f"{BASE}/account/order-history"
    
    # API эндпоинты
    API_REGISTER = f"{BASE}/api/auth/register"
    API_LOGIN = f"{BASE}/api/auth/login"
    API_USER = f"{BASE}/api/auth/user"