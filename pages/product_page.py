
from pages.base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def get_product_name_initial(self):
        product_name_initial = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return product_name_initial

    def get_product_price_initial(self):
        product_price_initial = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return product_price_initial

    def can_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name_final(self):
        product_name_final = self.browser.find_element(*ProductPageLocators.BOOK_NAME_FINAL)
        return product_name_final

    def get_product_price_final(self):
        product_price_final = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_FINAL)
        return product_price_final

    def compare_names(self, product_name_final, product_name_initial):
        a = product_name_initial
        b = product_name_final
        assert a == b, f'error in product name'

    def compare_prices(self, product_price_final, product_price_initial):
        a = product_price_final
        b = product_price_initial
        assert a == b, f'error in price'