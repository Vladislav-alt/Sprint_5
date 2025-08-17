import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture
def driver():
    # Путь к драйверу через переменные окружения
    driver_path = os.getenv('CHROME_DRIVER_PATH', 'chromedriver') 
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
