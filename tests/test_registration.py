import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestRegistration:
    @pytest.mark.parametrize(
        "name, email, password, expected",
        [
            ("Тест", "test@test.ru", "123456", True),
            ("", "test@test.ru", "123456", False),
            ("Тест", "invalid_email", "123456", False),
            ("Тест", "test@test.ru", "123", False),
        ],
    )
    def test_registration(self, driver, name, email, password, expected):
        """Тестирование регистрации с разными наборами данных"""
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Заполнение формы
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_SUBMIT).click()

        # Проверка результата
        if expected:
            WebDriverWait(driver, 10).until(EC.url_contains("login"))
        else:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.REG_ERROR)
            )
