from LoginPage import LoginProgram, CountAndWriteLetter, ReadLetters
from selenium.common.exceptions import NoSuchElementException
import allure


class TestProgram:
    @allure.title('Тест логина')
    @allure.feature('Login')
    @allure.story('Вводим логин')
    def test_login(self, browser):
        login_page = LoginProgram(browser)
        login_page.go_to_site()
        login_page.login()
        login_page.password()

    @allure.title('Тест подсчета писем')
    @allure.feature('Count letters')
    @allure.story('Считаем письма')
    def test_count_letter(self, browser):
        count_page = CountAndWriteLetter(browser)
        count_page.quantity_letters()
        count_page.write_letter()
        try:
            xpath_for_vhod = browser.find_element_by_xpath("//span[@class='badge__text']")
            for i in range(1, 10):
                if i == xpath_for_vhod.text:
                    assert browser.title == f'({i}) Входящие - Почта Mail.ru', "Ошибка заголовка"
        except NoSuchElementException:
            assert browser.title == 'Входящие - Почта Mail.ru'


    @allure.title('Тест чтения писем')
    @allure.feature('Read letters')
    @allure.story('Читаем письма')
    def test_read_letters(self, browser):
        read_letters = ReadLetters(browser)
        read_letters.read_letters()
