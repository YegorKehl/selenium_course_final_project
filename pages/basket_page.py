from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self) -> None:
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "Basket isn't empty"
