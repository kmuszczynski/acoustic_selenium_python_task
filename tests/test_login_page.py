import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.login_page import LoginPage


class TestLogin:

    @pytest.mark.positive
    @pytest.mark.login
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

    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.parametrize(
        "username, password, expected_error_message",
        [("sock_thief1","strongpassword","User does not exist."),
         ("sock_thief","wrong_password","Wrong password.")]
    )
    def test_negative_login(self, username, password, expected_error_message):
        # init driver and page object
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        login_page = LoginPage(driver)

        # open page
        login_page.open()

        # try to log in with incorrect username/password
        login_page.log_in(username, password)

        # assert alert text is correct
        text = login_page.read_alert_text()
        assert text == expected_error_message, f"Expected '{expected_error_message}' but got '{text}' instead"

