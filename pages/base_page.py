from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):  # экземпляр драйвера и url адрес
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what): #перехват исключения
        try: #два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True