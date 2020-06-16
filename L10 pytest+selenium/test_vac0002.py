from conftest import driver
from selenium import webdriver


class TestVacation:

    def test_search(self, driver):
        # constants
        value_for_search = 'Сити'
        url = 'https://www.cian.ru/vacancies/'
        root_button = '+ Опубликовать вакансию бесплатно'

        driver.get(url)

        # locators
        button_search = driver.find_element_by_xpath('//button[contains(text(), "Найти")]')
        input_for_name = driver.find_element_by_xpath('//input[@placeholder="Название компании"]')



        assert root_button in driver.page_source

        input_for_name.clear()
        input_for_name.send_keys(value_for_search)
        button_search.click()

        company_names = driver.find_elements_by_xpath('//a[contains(@href,"company")]')
        result = [item.text for item in company_names]
        for i in result:
            print(i)
            assert i.find(value_for_search)
