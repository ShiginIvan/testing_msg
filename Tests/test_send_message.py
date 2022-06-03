from pages.LoginPage import ActionLogin
from pages.MainPage import ActionMain
from pages.MessageCreatePage import ActionMessageCreate
from pages.MessageCreateStatusPage import CheckMessageCreateStatus
from pages.MessageCreateStatusPage import ActionMessageCreateStatus
from pages.DataMessagesPage import CheckDataMessages
import pytest
import allure
from allure_commons.types import AttachmentType


@allure.title('Отправка схемой default и проверка информации на странице статуса сообщения')
@allure.severity('NORMAL')
@pytest.mark.parametrize('title, message, address', [('заголовок', 'сообщение', '79101234567')])
def test_send_default_page_create_status(browser, title, message, address):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_default(title, message, address)
    message_create_status_page = CheckMessageCreateStatus(browser)
    check = message_create_status_page.check_message_status()
    assert 'Создание сообщений успешно: Отправлено сообщений: 1' in check, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)


@allure.title('Отправка схемой default и проверка статуса на странице сообщений')
@allure.severity('NORMAL')
@pytest.mark.parametrize('title, message, address',[('заголовок', 'сообщение', '79101234567'),
                                                    ('check', 'mess', '79101234569'),
                                                    ('!', '@', '79101234560')])
def test_send_default_page_data_messages(browser, title, message, address):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_default(title, message, address)
    message_create_page = ActionMessageCreateStatus(browser)
    message_create_page.open_data_messages()
    data_messages_page = CheckDataMessages(browser)
    check = data_messages_page.check_message_status()
    assert 'Отложено' in check, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)

@pytest.mark.skip
@allure.title('Отправка схемой push и проверка информации на странице статуса сообщения')
@allure.severity('NORMAL')
@pytest.mark.parametrize('title, message, address', [('заголовок', 'сообщение', '79101234567')])
def test_send_push_page_create_status(browser, title, message, address):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_schema(title, message, address, schema='push')
    message_create_status_page = CheckMessageCreateStatus(browser)
    check = message_create_status_page.check_message_status()
    assert 'Создание сообщений успешно: Отправлено сообщений: 1' in check, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)

@pytest.mark.skip
@allure.title('Отправка схемой push и проверка статуса на странице сообщений')
@allure.severity('NORMAL')
@pytest.mark.parametrize('title, message, address', [('заголовок', 'сообщение', '79101234567'),
                                                     ('check', 'mess', '79101234569'),
                                                     ('!', '@', '79101234560')])
def test_send_push_page_data_messages(browser,title, message, address):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_schema(title, message, address, schema='push')
    message_create_page = ActionMessageCreateStatus(browser)
    message_create_page.open_data_messages()
    data_messages_page = CheckDataMessages(browser)
    check = data_messages_page.check_message_status()
    assert 'Отложено' in check, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)
