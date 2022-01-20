from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_substring = 'login'
        #   проверка на корректный url адрес
        assert (url_substring in self.url), f'url != login_url expected'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), f'No Login_form found on login_page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_REG_BUTTON), f'No Registration_form found on login_page'

