from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)  # star (*) unpacks a tuple

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_visible(locator, time)
        self._find(locator).click()

    def _wait_until_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_clickable(self, locator: tuple, time: int = 10) -> WebElement:
        wait = WebDriverWait(self._driver, time)
        return wait.until(ec.element_to_be_clickable(locator))

    def _is_displayed(self, locator: tuple, time: int = 10) -> bool:
        wait = WebDriverWait(self._driver, time)
        try:
            return wait.until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            return False
