from conftest import driver
from pages.page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class VacanciesLocators:
    BUTTON_SEARCH = (By.XPATH, '//button[contains(text(), "Найти")]')
    INPUT_FOR_COMPANY_NAME = (By.XPATH, '//input[@placeholder="Название компании"]')
    COMPANY_NAMES = (By.XPATH, '//a[contains(@href,"company")]')


class VacanciesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.vacancies_url = 'vacancies/'

    def go_to_vacancies(self):
        return self.driver.get(self.base_url + self.vacancies_url)

    def enter_word(self, word):
        search_field = self.find_element(VacanciesLocators.INPUT_FOR_COMPANY_NAME)
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def click_on_search_button(self):
        return self.find_element(VacanciesLocators.BUTTON_SEARCH).click()

    def find_all_company_names(self):
        result = [item.text for item in self.find_elements(VacanciesLocators.COMPANY_NAMES)]
        return result


