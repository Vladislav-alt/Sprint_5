from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_logout(driver):
    """Тест выхода из аккаунта"""
    # Вход в систему
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.AUTH_EMAIL).send_keys("vladpotapov28111@yandex.ru")
    driver.find_element(*Locators.AUTH_PASS).send_keys("qwerty")
    driver.find_element(*Locators.AUTH_BUTTON).click()
    
    # Переход в ЛК
    WebDriverWait(driver, 10).until(
        EC.url_contains("account")
    )
    
    # Выход
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    
    # Проверка выхода
    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )
