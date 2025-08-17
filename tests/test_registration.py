import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from config.urls import Urls

class TestRegistration:
    @pytest.mark.parametrize("name,email,password", [
        ("Тест", "test@test.ru", "123456"),
    ])
    def test_successful_registration(self, driver, name, email, password):
        """Тест успешной регистрации"""
        driver.get(Urls.REGISTER)
        
        # Заполнение формы
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_SUBMIT).click()
        
        # Проверка успешной регистрации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.LOGIN)
        )
        assert driver.current_url == Urls.LOGIN

    @pytest.mark.parametrize("name,email,password,expected_error", [
        ("", "test@test.ru", "123456", "Некорректное имя"),
        ("Тест", "invalid_email", "123456", "Некорректный email"),
        ("Тест", "test@test.ru", "123", "Некорректный пароль"),
    ])
    def test_failed_registration(self, driver, name, email, password, expected_error):
        """Тест неудачной регистрации"""
        driver.get(Urls.REGISTER)
        
        # Заполнение формы
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_SUBMIT).click()
        
        # Проверка ошибки
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.NAME_ERROR)
        )
        assert expected_error in error.text