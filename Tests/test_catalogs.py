from pages.LoginPage import ActionLogin
from pages.MainPage import ActionMain
from pages.CatalogsDepartmentsPage import CheckDepartments
from pages.CatalogsDepartmentPage import ActionDepartment
from pages.CatalogsDepartmentsPage import ActionDepartments
import pytest
import allure
from allure_commons.types import AttachmentType

@allure.title('Создание справочника: Подразделения финансового учета')
@allure.severity('NORMAL')
@pytest.mark.parametrize('code, name', [('123', 'Бухгалтерия')])
def test_create_departments(browser, code, name):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_departments()
    departmets_page = ActionDepartments(browser)
    departmets_page.open_create_department()
    departmet_page = ActionDepartment(browser)
    departmet_page.enter_code_and_name(code, name)
    departmets_page = CheckDepartments(browser)
    check_create = departmets_page.check_new_department()
    assert code and name in check_create, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)
    departmets_page = ActionDepartments(browser)
    departmets_page.open_new_department()
    departmet_page = ActionDepartment(browser)
    departmet_page.delete_department()
    departmets_page = CheckDepartments(browser)
    check_delete = departmets_page.check_not_found_department()
    assert 'Не найдено ни одного подразделения' in check_delete, allure.attach(browser.get_screenshot_as_png(), name="FAILED", attachment_type=AttachmentType.PNG)


