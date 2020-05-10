from .pages.login_page import LoginPage


LOGIN_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"


def test_login_page_should_contain_login_and_registration_forms(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.should_be_login_page()
