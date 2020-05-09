from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
            "User icon is not presented, probably unauthorised user"

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BUTTON), "Basket button is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
