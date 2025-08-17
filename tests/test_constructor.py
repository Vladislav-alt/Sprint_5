import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from config.urls import Urls

class TestConstructor:
    @pytest.mark.parametrize("section_name,section_locator", [
        ("Булки", Locators.BUNS_SECTION),
        ("Соусы", Locators.SAUCES_SECTION),
        ("Начинки", Locators.FILLINGS_SECTION)
    ])
    def test_constructor_section_switch(self, driver, section_name, section_locator):
        """Тест переключения разделов конструктора"""
        driver.get(Urls.MAIN)
        
        section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(section_locator)
        )
        section.click()
        
        active_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert section_name in active_section.text