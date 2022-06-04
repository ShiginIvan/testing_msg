import settings
import pytest
from selenium import webdriver

NameBrowser = settings.Browser_name
NamePlatform = settings.Platform_name
HeadlessMode = settings.HEADLESS_MODE
HubAddress = settings.HUB_ADDRESS

def capabalilty_browsers(NameBrowser, NamePlatform):
    if NameBrowser == 'FIREFOX' and NamePlatform == 'WINDOWS':
        capability = {'browserName': 'firefox', 'platform': 'WINDOWS'}
    if NameBrowser == 'FIREFOX' and NamePlatform == 'LINUX':
        capability = {'browserName': 'firefox', 'platform': 'LINUX'}
    if NameBrowser == 'CHROME' and NamePlatform == 'WINDOWS':
        capability = {'browserName': 'chrome', 'platform': 'WINDOWS'}
    if NameBrowser == 'CHROME' and NamePlatform == 'LINUX':
        capability = {'browserName': 'chrome', 'platform': 'LINUX'}
    return capability

def option_browsers(webdriver, HeadlessMode, NameBrowser):
    if NameBrowser == 'FIREFOX' and HeadlessMode == 1:
        options_browser = webdriver.FirefoxOptions()
        options_browser.add_argument('--headless')
        options_browser.add_argument('--no-sandbox')
        options_browser.add_argument('-–disable-gpu')
        options_browser.add_argument("--width=1920")
        options_browser.add_argument("--height=1080")
    if NameBrowser == 'CHROME' and HeadlessMode == 1:
        options_browser = webdriver.ChromeOptions()
        options_browser.add_argument('--headless')
        options_browser.add_argument('--no-sandbox')
        options_browser.add_argument('-–disable-gpu')
        options_browser.add_argument("--window-size=1920,1080")
    if NameBrowser == 'CHROME' and HeadlessMode == 0:
        options_browser = webdriver.ChromeOptions()
        options_browser.add_argument("--window-size=1920,1080")
    if NameBrowser == 'FIREFOX' and HeadlessMode == 0:
        options_browser = webdriver.FirefoxOptions()
        options_browser.add_argument("--width=1920")
        options_browser.add_argument("--height=1080")
    return options_browser

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Remote(command_executor=(HubAddress + '/wd/hub'),
                              desired_capabilities=capabalilty_browsers(NameBrowser, NamePlatform),
                              options=option_browsers(webdriver, HeadlessMode, NameBrowser))
    yield driver
    driver.quit()



