from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class HomePage(BasePage):
    __url = "https://www.demoblaze.com/index.html"
    __login_button = (By.ID, "login2")
    __username_field = (By.ID, "loginusername")
    __password_field = (By.ID, "loginpassword")
    __login_submit_button = (By.XPATH, "//button[@onClick='logIn()']")
    __logout_button = (By.ID, "logout2")
    __welcome_button = (By.ID, "nameofuser")
    __correct_username = "sock_thief"
    __correct_password = "strongpassword"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._driver.get(self.__url)

    def log_in(self, username: str = __correct_username, password: str = __correct_password):
        super()._click(self.__login_button)
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__login_submit_button)

    def log_out_displayed(self):
        return super()._is_displayed(self.__logout_button)

    def welcome_displayed(self):
        return super()._is_displayed(self.__welcome_button)
