import time

import pytest

from pages.product_page import ProductPage
@pytest.mark.parametrize('promo_end_link', [*range(7), pytest.param(7,marks=pytest.mark.xfail), *range(8,10)] )
def test_guest_can_add_product_to_basket(browser, promo_end_link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    link_final = f'{link}{promo_end_link}'
    print(link_final)
    page = ProductPage(browser, link_final)
    page.open()
    name_initial = page.get_product_name_initial()
    a = name_initial.text
    price_initial = page.get_product_price_initial()
    b = price_initial.text
    page.can_add_product_to_basket()
    page.solve_quiz_and_get_code()

    name_final = page.get_product_name_final() # вытаскиваем название продукта на стр
    a1 = name_final.text
    price_final = page.get_product_price_final() # вытаскиваем цену продукта на стр
    b1 = price_final.text


    page.compare_names(a, a1)
    page.compare_prices(b, b1)
