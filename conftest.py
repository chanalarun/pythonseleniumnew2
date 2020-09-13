import pytest

from utils import utils

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")

    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="C:/Users/hp/PycharmProjects/pyhonseleniymframe/drivers/geckodriver.exe")

    driver.get(utils.URL)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("test completed")