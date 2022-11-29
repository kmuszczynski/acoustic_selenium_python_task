from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class CartPage(BasePage):
    __url = "https://www.demoblaze.com/cart.html"
    __form = (By.ID, "orderModal")
    __name_field = (By.ID, "name")
    __country_field = (By.ID, "country")
    __city_field = (By.ID, "city")
    __card_field = (By.ID, "card")
    __month_field = (By.ID, "month")
    __year_field = (By.ID, "year")
    __purchase_button = (By.XPATH, "//button[@onClick='purchaseOrder()']")
    __place_order_button = (By.XPATH, "//button[@data-target='#orderModal']")
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
