from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_BUTTON = (By.NAME, "login_submit")

    SUBMIT_REG_BUTTON = (By.NAME, "registration_submit")