from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There isn't 'login' substring in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "Login e-mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD),\
            "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
        assert self.is_element_present(*LoginPageLocators.RESET_PASSWORD_LINK),\
            "Reset password link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD),\
            "Register e-mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD1), \
            "Register first password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD2), \
            "Register second password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
