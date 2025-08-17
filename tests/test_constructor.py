from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators

def test_constructor_sections(driver):
    """Тест переключения разделов конструктора"""
    driver.get("https://stellarburgers.nomoreparties.site")
    
    sections = [
        ("Булки", Locators.BUNS_SECTION),
        ("Соусы", Locators.SAUCES_SECTION),
        ("Начинки", Locators.FILLINGS_SECTION)
    ]
    
    for name, locator in sections:
        # Ожидание и клик по разделу
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        
        # Проверка активного раздела
        active_tab = driver.find_element(*Locators.ACTIVE_SECTION)
        assert name in active_tab.text, f"Раздел {name} не стал активным"