from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_login_main_button(driver):
    """Тест входа через кнопку 'Войти в аккаунт' на главной"""
    driver.get("https://stellarburgers.nomoreparties.site")

    # Клик по кнопке входа
    driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

    # Заполнение формы
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.AUTH_EMAIL)
    ).send_keys("vladpotapov28111@yandex.ru")

    driver.find_element(*Locators.AUTH_PASS).send_keys("qwerty")
    driver.find_element(*Locators.AUTH_BUTTON).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(EC.url_contains("account"))


def test_login_personal_account_button(driver):
    """Тест входа через кнопку 'Личный кабинет'"""
    driver.get("https://stellarburgers.nomoreparties.site")

    # Клик по кнопке личного кабинета
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    # Заполнение формы
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.AUTH_EMAIL)
    ).send_keys("vladpotapov28111@yandex.ru")

    driver.find_element(*Locators.AUTH_PASS).send_keys("qwerty")
    driver.find_element(*Locators.AUTH_BUTTON).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(EC.url_contains("account"))
