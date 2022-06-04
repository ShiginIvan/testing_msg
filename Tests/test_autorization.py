import time
from pages.LoginPage import ActionLogin
from pages.LoginPage import CheckLogin
from pages.MainPage import CheckMain
import pytest
import allure
from allure_commons.types import AttachmentType
import settings

@allure.title('Проверка сообщения: Неверная учетная запись или пароль при неуспешной авторизации с неверным паролем')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('login, password', [('admin', '0000')])
def test_wrong_password(browser, login, password):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.enter_login_and_password(login, password)
    time.sleep(1)
    login_page = CheckLogin(browser)
    message = login_page.check_wrong_login_message()
    if settings.Platform_name == 'LINUX':
        assert 'Bad credentials' in message, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)
    else:
        assert 'Неверная учетная запись или пароль' in message, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)

@allure.title('Проверка сообщения: Неверные учетные данные пользователя при неуспешной авторизации с неверным логином')
@pytest.mark.parametrize('login, password', [('admin1', 'zj#KqU1')])
@allure.severity(allure.severity_level.MINOR)
def test_wrong_login(browser, login, password):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.enter_login_and_password(login, password)
    time.sleep(1)
    login_page = CheckLogin(browser)
    message = login_page.check_wrong_login_message()
    if settings.Platform_name == 'LINUX':
        assert 'Bad credentials' in message, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)
    else:
        assert 'Неверные учетные данные пользователя' in message, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)


@allure.title('Проверка успешной авторизации')
@pytest.mark.parametrize('login, password', [('admin', 'admin')])
@allure.severity(allure.severity_level.MINOR)
def test_success(browser, login, password):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.enter_login_and_password(login, password)
    main_page = CheckMain(browser)
    title = main_page.check_title()
    assert "Сервер сообщений" in title, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)

