from BaseApp import BasePage
from selenium.webdriver.common.by import By


class ChromeLocators:
    LOCATOR_LOGIN_BOX = (By.CLASS_NAME, "input-0-2-77")
    LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, "inner-0-2-89.innerTextWrapper-0-2-90")
    LOCATOR_PASSWORD_BOX = (By.CLASS_NAME, "input-0-2-77.withIcon-0-2-78")
    LOCATOR_PASSWORD_BUTTON = (By.CLASS_NAME, "inner-0-2-89.innerTextWrapper-0-2-90")
    LOCATOR_COUNT_LETTERS = (By.CLASS_NAME, "ll-sj__normal")
    LOCATOR_WRITE_LETTER_BUTTON = (By.CLASS_NAME, "compose-button__wrapper")
    LOCATOR_MAIL_WRITE_LETTER = (By.CLASS_NAME, "container--zU301")
    LOCATOR_TOPIC_LETTER = (By.XPATH, "//input[@name='Subject']")
    LOCATOR_TEXT_LETTER = (By.CSS_SELECTOR,
                           "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
    LOCATOR_SEND_LETTER_BUTTON = (By.CLASS_NAME, "button2__wrapper")
    LOCATOR_QUIT_LETTER_BUTTON = (By.XPATH,
                                  "//span[@title='Закрыть']//span[@class='button2__wrapper button2__wrapper_centered']")
    LOCATOR_READ_LETTERS_BUTTON = (By.XPATH,
                                   "/html[1]/body[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/span[2]/div[1]/span[1]/span[1]")
    LOCATOR_VERIFY_READ_LETTERS_BUTTON = (By.XPATH,
                                          "//span[@class='button2 button2_base button2_primary button2_fluid button2_hover-support']//span[@class='button2__wrapper']")


class LoginProgram(BasePage):
    def login(self):
        self.driverwait(ChromeLocators.LOCATOR_LOGIN_BOX).send_keys('test_mail_for_simbir3')
        self.driverwait(ChromeLocators.LOCATOR_LOGIN_BUTTON).click()

    def password(self):
        self.driverwait(ChromeLocators.LOCATOR_PASSWORD_BOX).send_keys('Mycatisnike1')
        self.driverwait(ChromeLocators.LOCATOR_PASSWORD_BUTTON).click()


class CountAndWriteLetter(BasePage):
    def quantity_letters(self):
        counter = self.count_letters(ChromeLocators.LOCATOR_COUNT_LETTERS)
        self.quantity = 0
        for i in counter:
            if i.text == 'Simbirsoft Тестовое задание' or 'Simbirsoft Тестовое задание.Сайганов':
                self.quantity += 1

    def write_letter(self):
        self.driverwait(ChromeLocators.LOCATOR_WRITE_LETTER_BUTTON).click()
        self.driverwait(ChromeLocators.LOCATOR_MAIL_WRITE_LETTER).send_keys('test_mail_for_simbir3@mail.ru')
        self.driverwait(ChromeLocators.LOCATOR_TOPIC_LETTER).send_keys('Simbirsoft Тестовое задание.Сайганов')
        self.driverwait(ChromeLocators.LOCATOR_TEXT_LETTER).send_keys('Количество писем: ' + str(self.quantity))
        self.driverwait(ChromeLocators.LOCATOR_SEND_LETTER_BUTTON).click()
        self.driverwait(ChromeLocators.LOCATOR_QUIT_LETTER_BUTTON).click()


class ReadLetters(BasePage):
    def read_letters(self):
        self.driverwait(ChromeLocators.LOCATOR_READ_LETTERS_BUTTON).click()
        self.driverwait(ChromeLocators.LOCATOR_VERIFY_READ_LETTERS_BUTTON).click()
