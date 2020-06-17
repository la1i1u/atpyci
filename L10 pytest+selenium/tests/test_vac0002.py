from conftest import driver
from selenium import webdriver
from pages.vacancies_page import VacanciesPage


class TestVacation:

    def test_choose_region(self,driver):
        needed_region = 'Кубинка'
        vacancies_main_page = VacanciesPage(driver)
        vacancies_main_page.go_to_vacancies()
        vacancies_main_page.enter_region_for_keys(needed_region)
        vacancies_main_page.click_on_needed_region(needed_region)
        vacancies_main_page.click_on_search_button()
        result = vacancies_main_page.find_all_regions()
        for i in result:
            print("нашла")
            assert i.find(needed_region) or i == needed_region
        vacancies_main_page.click_on_show_contacts()
        assert vacancies_main_page.find_phone()

    def test_search(self, driver):
        # constants
        word = 'Центральный'

        vacancies_main_page = VacanciesPage(driver)
        vacancies_main_page.go_to_vacancies()
        vacancies_main_page.enter_word_in_company_names_input(word)
        vacancies_main_page.click_on_search_button()
        result = vacancies_main_page.find_all_company_names()

        for i in result:
            assert i.find(word) or i == word
