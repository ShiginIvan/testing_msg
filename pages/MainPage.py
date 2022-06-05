from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    title_main_page = (By.CSS_SELECTOR, 'body > div > h2')
    messages_menu = (By.CSS_SELECTOR, '#messagesMenuLink')
    messages_menu_create_message = (By.CSS_SELECTOR,'#navbarNavDropdown > ul.navbar-nav.me-auto > li:nth-child(1) > ul > li:nth-child(7) > a')
    catalogs_menu = (By.ID, 'dicMenuLink')
    catalogs_menu_departments = (By.CSS_SELECTOR, '#navbarNavDropdown > ul.navbar-nav.me-auto > li:nth-child(4) > ul > li:nth-child(1) > a')



class CheckMain(BasePage):
    def check_title(self):
        search_title = self.find_element(SearchLocators.title_main_page)
        return search_title.text


class ActionMain(BasePage):
    def open_create_message(self):
        messages_menu = self.find_element(SearchLocators.messages_menu)
        messages_menu.click()
        messages_menu_create_message = self.find_element(SearchLocators.messages_menu_create_message)
        messages_menu_create_message.click()

    def open_departments(self):
        catalogs_menu = self.find_element(SearchLocators.catalogs_menu)
        catalogs_menu.click()
        catalogs_menu_departments = self.find_element(SearchLocators.catalogs_menu_departments)
        catalogs_menu_departments.click()

