from conftest import driver
from pages.page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class VacanciesLocators:

    # Кнопки
    BUTTON_SEARCH = (By.XPATH, '//button[contains(text(), "Найти")]')
    BUTTON_ADD_VACANCIES = (By.XPATH, '//button[contains(text(), "+ Опубликовать вакансию бесплатно")]')
    BUTTON_SHOW_CONTACTS = (By.XPATH, '//button[contains(text(), "Показать контакты")]')
    BUTTON_FEEDBACK = (By.XPATH, '//button[contains(text(), "Что вы думаете об этом разделе?")]')
    BUTTON_MORE_DESCRIPTION = (By.XPATH, '//button//span[contains(text(), "Развернуть описание")]')
    BUTTON_LESS_DESCRIPTION = (By.XPATH, '//button//span[contains(text(), "Свернуть описание")]')

    # Поисковые элементы
    INPUT_FOR_COMPANY_NAME = (By.XPATH, '//input[@placeholder="Название компании"]')
    INPUT_FOR_PRICE_FROM = (By.XPATH, '//div[span[contains(text(), "Зарплата")]]//input[@placeholder="от"]')
    INPUT_FOR_PRICE_TO = (By.XPATH, '//div[span[contains(text(), "Зарплата")]]//input[@placeholder="до"]')
    INPUT_FOR_REGION = (By.XPATH, '//div[contains(@class,"region")]//input')
    SEARCH_POPUP_WITH_REGIONS = (By.XPATH, '//div[contains(@class,"popup_content")]//div')
    SEARCH_REGION = '//div[contains(@class,"popup_content")]//div[contains(text(), "{}")]'



    # Элементы на выдаче
    COMPANY_NAMES = (By.XPATH, '//a[contains(@href,"company")]')
    REGIONS_ON_RESULT = (By.XPATH, '//div[contains(text(), "Город")]/following-sibling::div[contains(@class, '
                                   '"bold_text")]')
    PHONE = (By.XPATH, '//div[contains(@class, "phone")]')


class VacanciesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.vacancies_url = 'vacancies/'

    # Переход на страницу вакансий
    def go_to_vacancies(self):
        return self.driver.get(self.base_url + self.vacancies_url)

    # Ввод значений в поиск
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

    def enter_region_for_keys(self,selected_region):
        region = self.find_element(VacanciesLocators.INPUT_FOR_REGION)
        region.clear()
        region.send_keys(selected_region)
        return region

    # Поиск элемента в попапе региона
    def click_on_needed_region(self, region):
        locator = (By.XPATH, VacanciesLocators.SEARCH_REGION.format(region))
        needed_region = self.find_element(locator)
        needed_region.click()

    #  Кнопка поиска
    def click_on_search_button(self):
        return self.find_element(VacanciesLocators.BUTTON_SEARCH).click()

    # Поиск элементов в выдаче
    def find_all_company_names(self):
        result = [item.text for item in self.find_elements(VacanciesLocators.COMPANY_NAMES)]
        return result

    def find_all_regions(self):
        result = [item.text for item in self.find_elements(VacanciesLocators.REGIONS_ON_RESULT)]
        return result

    def click_on_show_contacts(self):
        return self.find_element(VacanciesLocators.BUTTON_SHOW_CONTACTS).click()

    def find_phone(self):
        result = self.find_element(VacanciesLocators.PHONE)
        return result


