import time

from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SearchLocators:
    field_code = (By.ID, 'code')
    field_name = (By.ID, 'name')
    button_delete = (By.CSS_SELECTOR, 'body > div > form > div > div > a.btn.btn-outline-danger.btn-md')
    button_delete_madal = (By.XPATH, '/html/body/div[1]/div[1]/form/div/div/div[3]/button[1]')


class ActionDepartment(BasePage):
    def enter_code_and_name(self, code, name):
        field_code = self.find_element(SearchLocators.field_code)
        field_code.send_keys(code)
        field_name = self.find_element(SearchLocators.field_name)
        field_name.send_keys(name)
        field_name.send_keys(Keys.ENTER)

    def delete_department(self, browser):
        button_delete = self.find_element(SearchLocators.button_delete)
        button_delete.click()
        button_delete_madal = self.find_element(SearchLocators.button_delete_madal)
        test_1 = ActionChains(browser).move_to_element(button_delete_madal).click(button_delete_madal)
        time.sleep(1)
        test_1.perform()