from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    button_create_1 = (By.CLASS_NAME, 'col-md-auto')
    new_department = (By.CSS_SELECTOR, '#clients > tbody')
    code = (By.CSS_SELECTOR, '#clients > tbody > tr > td:nth-child(1) > a')
    not_found_department = (By.XPATH, '/html/body/div/div[3]/div/div/div[1]/h4')



class CheckDepartments(BasePage):
    def check_new_department(self):
        new_department = self.find_element(SearchLocators.new_department)
        return new_department.text
    def check_not_found_department(self):
        not_found_depatment = self.find_element(SearchLocators.not_found_department)
        return not_found_depatment.text


class ActionDepartments(BasePage):
    def open_create_department(self):
        button_create_1 = self.find_element(SearchLocators.button_create_1)
        button_create_1.click()

    def open_new_department(self):
        code = self.find_element(SearchLocators.code)
        code.click()


