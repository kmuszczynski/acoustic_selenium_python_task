from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import ast

from page_objects.base_page import BasePage


class CartPage(BasePage):
    __url = "https://www.demoblaze.com/cart.html"

    # locators
    __form = (By.ID, "orderModal")
    __name_field = (By.ID, "name")
    __country_field = (By.ID, "country")
    __city_field = (By.ID, "city")
    __card_field = (By.ID, "card")
    __month_field = (By.ID, "month")
    __year_field = (By.ID, "year")
    __purchase_button = (By.XPATH, "//button[@onClick='purchaseOrder()']")
    __place_order_button = (By.XPATH, "//button[@data-target='#orderModal']")
    __thank_you_message = (By.XPATH, "//h2[.='Thank you for your purchase!']")
    __ok_button = (By.XPATH, "//button[.='OK']")
    __thank_you_prompt_p = (By.XPATH, "//p[@class='lead text-muted ']")

    # helper lists
    __form_fields = [__name_field, __country_field, __city_field, __card_field, __month_field, __year_field]
    __form_info_correct = ["Sock Thief", "Sockland", "New Socks", "0", "1", "2025"]

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._driver.get(self.__url)

    def place_order(self):
        super()._click(self.__place_order_button)
        for field, info in zip(self.__form_fields, self.__form_info_correct):
            super()._type(field, info)
        super()._click(self.__purchase_button)

    def thank_you_displayed(self):
        return super()._is_displayed(self.__thank_you_message)

    def click_ok(self):
        super()._click(self.__ok_button)

    @property
    def thank_you_prompt_text(self) -> dict:
        text = super()._find(self.__thank_you_prompt_p).text
        return dict(sub_string.split(': ') for sub_string in text.split('\n'))

