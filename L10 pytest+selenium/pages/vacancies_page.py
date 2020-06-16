from conftest import driver
from pages.page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class VacanciesLocators:
    BUTTON_SEARCH = (By.XPATH, '//button[contains(text(), "Найти")]')
    INPUT_FOR_COMPANY_NAME = (By.XPATH, '//input[@placeholder="Название компании"]')
    COMPANY_NAMES = (By.XPATH, '//a[contains(@href,"company")]')
    INPUT_FOR_PRICE_FROM = (By.XPATH, '//div[span[contains(text(), "Зарплата")]]//input[@placeholder="от"]')
    INPUT_FOR_PRICE_TO = (By.XPATH, '//div[span[contains(text(), "Зарплата")]]//input[@placeholder="до"]')


class VacanciesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.vacancies_url = 'vacancies/'

    #переход на страницу вакансий
    def go_to_vacancies(self):
        return self.driver.get(self.base_url + self.vacancies_url)

    #ввод значений в поиск
    def enter_word_in_company_names_input(self, word):
        search_field = self.find_element(VacanciesLocators.INPUT_FOR_COMPANY_NAME)
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def enter_value_in_price_from(self, price):
        price_from = self.find_element(VacanciesLocators.INPUT_FOR_PRICE_FROM)
        price_from.clear()
        price_from.send_keys(price)
        return price_from

    def enter_value_in_price_to(self, price):
        price_to = self.find_element(VacanciesLocators.INPUT_FOR_PRICE_TO)
        price_to.clear()
        price_to.send_keys(price)
        return price_to

    def choose_city(self):
        print('булочки')

    #кнопка поиска
    def click_on_search_button(self):
        return self.find_element(VacanciesLocators.BUTTON_SEARCH).click()

    #поиск элементов в выдаче
    def find_all_company_names(self):
        result = [item.text for item in self.find_elements(VacanciesLocators.COMPANY_NAMES)]
        return result


