import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.data_generator import generate_email, generate_password


@pytest.fixture
def driver():
    service = Service(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def random_credentials():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "name": "AutotestUser",
    }
