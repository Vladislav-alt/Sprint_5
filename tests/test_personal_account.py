from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from config.urls import Urls

class TestPersonalAccount:
    def test_logout(self, driver):
        """Тест выхода из аккаунта"""
        # Вход в систему
        driver.get(Urls.LOGIN)
        driver.find_element(*Locators.AUTH_EMAIL).send_keys("vladpotapov28111@yandex.ru")
        driver.find_element(*Locators.AUTH_PASS).send_keys("qwerty")
        driver.find_element(*Locators.AUTH_BUTTON).click()
        
        # Переход в ЛК
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.MAIN)
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Выход
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        ).click()
        
        # Проверка выхода
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.LOGIN)
        )
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.AUTH_FORM)
        )