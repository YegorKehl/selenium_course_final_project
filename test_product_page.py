from .pages.product_page import ProductPage
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_name()
    product_page.should_be_color_price()
    product_page.should_be_success_alert(product_page.product_name())
    product_page.should_be_info_alert(product_page.color_price())
    sleep(10)
