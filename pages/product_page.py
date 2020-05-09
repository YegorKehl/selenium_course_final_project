from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def color_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.COLOR_PRICE).text

    def product_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_color_price(self):
        assert self.is_element_present(*ProductPageLocators.COLOR_PRICE), "There is no color price under product name"

    def should_be_info_alert(self, price: str):
        assert self.is_element_present(*ProductPageLocators.INFO_ALERT), "There is no info alert"
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_IN_INFO_ALERT),\
            "There is no basket total in info alert"
        basket_total_in_info_alert = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_IN_INFO_ALERT)
        assert price in basket_total_in_info_alert.text,\
            "Price of product is not equal to basket total in info alert"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "There is no product name"

    def should_be_success_alert(self, product_name: str):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), "There is no success alert"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_ALERT),\
            "There is no product name in success alert"
        product_name_in_success_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_ALERT)
        assert product_name == product_name_in_success_alert.text,\
            "Product name in product page and in success alert is not equal"
