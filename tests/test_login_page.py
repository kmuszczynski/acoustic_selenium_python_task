from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

from page_objects.login_page import LoginPage


class TestPositive:
    def test_positive_login(self):
        # init driver and page objects
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        login_page = LoginPage(driver)

        # go to the page
        login_page.open()

        # use pre-existing user: sock_thief, strongpassword
        # log in
        login_page.log_in()

        # # verify that "Welcome {username}" is visible
        assert login_page.welcome_displayed(), "Welcome button should be displayed but isn't"

        # # verify that "Log out" button is visible
        assert login_page.log_out_displayed(), "Log out button should be displayed but isn't"
