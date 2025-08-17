class Locators:
    # Регистрация
    REG_NAME = ("xpath", "//label[contains(.,'Имя')]/following-sibling::input")
    REG_EMAIL = ("xpath", "//label[contains(.,'Email')]/following-sibling::input")
    REG_PASSWORD = ("xpath", "//input[@type='password']")
    REG_SUBMIT = ("xpath", "//button[contains(.,'Зарегистрироваться')]")
    REG_ERROR = ("xpath", "//p[contains(@class,'input__error')]")

    # Авторизация
    LOGIN_BUTTON_MAIN = ("xpath", "//button[contains(.,'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = ("xpath", "//p[contains(.,'Личный Кабинет')]")
    AUTH_EMAIL = ("xpath", "//input[@name='name']")
    AUTH_PASS = ("xpath", "//input[@type='password']")
    AUTH_BUTTON = ("xpath", "//button[contains(.,'Войти')]")

    # Конструктор
    BUNS_SECTION = ("xpath", "//span[contains(.,'Булки')]/..")
    SAUCES_SECTION = ("xpath", "//span[contains(.,'Соусы')]/..")
    FILLINGS_SECTION = ("xpath", "//span[contains(.,'Начинки')]/..")
    ACTIVE_SECTION = ("class name", "tab_tab_type_current__2BEPc")

    # Личный кабинет
    LOGOUT_BUTTON = ("xpath", "//button[contains(.,'Выход')]")
