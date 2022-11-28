from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
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
        self._driver = driver

    def _wait_for_clickable(self, locator: tuple, time: int = 10) -> WebElement:
        wait = WebDriverWait(self._driver, time)
        return wait.until(ec.element_to_be_clickable(locator))

    def _is_displayed(self, locator: tuple, time: int = 10) -> bool:
        wait = WebDriverWait(self._driver, time)
        try:
            return wait.until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def open(self):
        self._driver.get(self.__url)

    def log_in(self):
        self._wait_for_clickable(self.__login_button).click()
        self._wait_for_clickable(self.__username_field).send_keys(self.__correct_username)
        self._wait_for_clickable(self.__password_field).send_keys(self.__correct_password)
        self._wait_for_clickable(self.__login_submit_button).click()

    def log_out_displayed(self):
        return self._is_displayed(self.__logout_button)
