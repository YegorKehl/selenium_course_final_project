from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    RESET_PASSWORD_LINK = (By.CSS_SELECTOR, "#login_form a[href$='/password-reset/']")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_FIELD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    INFO_ALERT = (By.CSS_SELECTOR, ".alert-info")
    BASKET_TOTAL_IN_INFO_ALERT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    COLOR_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    PRODUCT_NAME_IN_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")

