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

        # # click login
        # driver.find_element(By.ID, "login2").click()
        #
        # # type username
        # wait = WebDriverWait(driver, 10)
        # # driver.find_element(By.ID, "loginusername").send_keys("sock_thief")
        # wait.until(ec.element_to_be_clickable((By.ID, "loginusername"))).send_keys("sock_thief")
        #
        # # type password
        # driver.find_element(By.ID, "loginpassword").send_keys("strongpassword")
        #
        # # click log in
        # driver.find_element(By.XPATH, "//button[@onClick='logIn()']").click()

        # log in
        login_page.log_in()

        # # verify that "Welcome {username}" is visible
        # welcome_locator = wait.until(ec.visibility_of_element_located((By.ID, "nameofuser")))
        # assert welcome_locator.is_displayed(), "Welcome button should be displayed, but isn't"

        # # verify that "Log out" button is visible
        # logout_locator = driver.find_element(By.ID, "logout2")
        # assert logout_locator.is_displayed(), "Logout button should be displayed, but isn't"
        assert login_page.log_out_displayed(), "Log out button should be displayed but isn't"
