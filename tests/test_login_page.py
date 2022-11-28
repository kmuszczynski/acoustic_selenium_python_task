from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestPositive:
    def test_positive_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # go to the page
        driver.get("https://www.demoblaze.com/index.html")

        # use pre-existing user: sock_thief, strongpassword

        # click login

        # type username

        # type password

        # verify that "Welcome {username}" is visible

        # verify that "Log out" button is visible
