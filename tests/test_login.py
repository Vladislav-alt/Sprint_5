from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from config.urls import Urls

class TestLogin:
    def test_login_via_personal_account_button(self, driver):
        """Тест входа через кнопку 'Личный кабинет'"""
        driver.get(Urls.MAIN)
        
        # Клик по кнопке личного кабинета
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Заполнение формы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.AUTH_EMAIL)
        ).send_keys("vladpotapov28111@yandex.ru")
        
        driver.find_element(*Locators.AUTH_PASS).send_keys("qwerty")
        driver.find_element(*Locators.AUTH_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.MAIN)
        )
        assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()