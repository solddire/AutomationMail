import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


@pytest.fixture(scope="session")
def browser():
    capabilities = DesiredCapabilities.CHROME
    driver = webdriver.Remote(
        command_executor='http://192.168.0.103:4444',
        desired_capabilities=capabilities
    )
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
