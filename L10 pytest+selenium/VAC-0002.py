from browserworks import driver
from selenium import webdriver


class TestVacation:

    def test_search(self, driver):
        driver.get('https://www.cian.ru/vacancies/')
        assert '+ Опубликовать вакансию бесплатно' in driver.page_source
        input_for_name = driver.find_element_by_xpath('//input[@placeholder="Название компании"]')
        input_for_name.clear()
        value_for_search = 'Сити'
        input_for_name.send_keys(value_for_search)
        button_search = driver.find_element_by_xpath('//button[contains(text(), "Найти")]')
        button_search.click()
        result = [item.text for item in driver.find_elements_by_xpath('//a[contains(@href,"company")]')]
        i = len(result)
        for i in result:
            assert i.find(value_for_search)
