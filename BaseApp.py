from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://account.mail.ru/login"
        self.quantity = 0

    def driverwait(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    def count_letters(self, locator):
        return WebDriverWait(self.driver, 50).until(ec.visibility_of_all_elements_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)
