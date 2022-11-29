import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.cart_page import CartPage


class TestPurchase:

    @pytest.mark.positive
    @pytest.mark.purchase
    @pytest.mark.debug
    def test_positive_purchase(self):
        # go to home page
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cart_page = CartPage(driver)

        # login? maybe? not needed. optional? skip for now

        # click any phone

        # verify the page changed?

        # click add to cart

        # dismiss alert

        # click cart button (in top navbar)
        # need to change the page object somehow?
        # ad hoc solution: don't click at all? just load new page?
        cart_page.open()

        # click "Place Order"
        cart_page.place_order()
        # fill the form
        # Name: Sock Thief
        # Country: Sockland
        # City: New Socks
        # Credit card: 0000000000000000
        # Month: 08
        # Year: 2025

        # click purchase

        # verify "Thank you for your purchase!" is displayed

        # click "OK"

        # uhh.... verify the cart is empty? maybe? skip for now

        """Notes on how to break the Place order form:
        name: numeric, script symbols
        country: same
        city: same
        credit card: non-numeric
        month: non-numeric, negative, > 12
        year: in the past, non-numeric, negative, too far in the future

        Question: Does it break if run in parallel? Does each window have its own session id?

        Is it too big? Should it be split into smaller bits? ;-;

        Additional tests:
        * check if delete (from cart) button works?
        * in place order form input stays, if you press cancel (and hide the form), check if it works correctly?
        """
        pass
