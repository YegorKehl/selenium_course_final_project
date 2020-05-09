from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from time import time, sleep
import pytest
import random
import string


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    def random_string(self, string_length=9) -> str:
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(string_length))

    # use bad practice, as it needed by task in 4.3.13
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        email = str(time()) + "@fakemail.org"
        password = self.random_string()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, self.product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.product_link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_be_product_name()
        product_page.should_be_color_price()
        product_page.should_be_success_alert(product_page.product_name())
        product_page.should_be_info_alert(product_page.color_price())


@pytest.mark.parametrize('promo', ["?promo=offer0",
                                   "?promo=offer1",
                                   "?promo=offer2",
                                   "?promo=offer3",
                                   "?promo=offer4",
                                   "?promo=offer5",
                                   "?promo=offer6",
                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                   "?promo=offer8",
                                   "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.implicitly_wait(2)
    product_page = ProductPage(browser, link+f"{promo}")
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_name()
    product_page.should_be_color_price()
    product_page.should_be_success_alert(product_page.product_name())
    product_page.should_be_info_alert(product_page.color_price())


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_link()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
