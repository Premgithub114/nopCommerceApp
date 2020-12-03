from selenium import webdriver
import time
import pytest
import unittest

from pageobjects.login_page import test_login
from Utilities.read_data import all_data

class test_main(unittest.TestCase):
    # We should not keep any data inside the test case. We should keep all data in one config folder
    # and import from that folder.
    baseurl = all_data.get_url()
    user_email = all_data.get_user_email()
    user_password = all_data.get_passw()

    @pytest.mark.sanity  # This test method is a Sanity test method
    def test_beforelogging(self):

        self.driver = webdriver.Chrome("C:/Users/Prem/PycharmProjects/page_object_model_1/drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        before_log_title = self.driver.title
        if before_log_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()

    @pytest.mark.sanity         # This test method is a Sanity test method
    @pytest.mark.regression     # This method is a regression test method
    def test_logging_in(self):

        self.driver = webdriver.Chrome("C:/Users/Prem/PycharmProjects/page_object_model_1/drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        time.sleep(2)
        self.obj1_login = test_login(self.driver)
        self.obj1_login.set_username(self.user_email)
        self.obj1_login.set_password(self.user_password)
        time.sleep(3)
        self.obj1_login.click_login()
        time.sleep(3)
        page_title = self.driver.title
        if page_title == "Dashboard / nopCommerce administrationn":
            assert True
            self.driver.close()

        else:
            # If the test method fails, we can generate the screenshot as below.
            self.driver.save_screenshot("C:/Users/Prem/PycharmProjects/Hybrid_FW/screenshots/" + "login_screenshot.png")
            assert False
            self.driver.close()


