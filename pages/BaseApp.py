from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from allure_commons.types import AttachmentType
import setings

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=2):
        try:
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), allure.attach(self.driver.get_screenshot_as_png(), name=f"{locator} NOT FOUND", attachment_type=AttachmentType.PNG))

    def go_to_site(self):
        return self.driver.get(setings.MSG_ADMIN)
