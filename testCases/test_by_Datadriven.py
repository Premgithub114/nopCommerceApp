from selenium import webdriver
import time
import pytest
import unittest

from pageobjects.login_page import test_login
from Utilities.read_data import all_data
from Utilities import xlutilities

class test_main_ddt_test(unittest.TestCase):
    # We should not keep any data inside the test case. We should keep all data in one config folder
    # and import from that folder.
    baseurl = all_data.get_url()
    path = "C:/Users/Prem/PycharmProjects/Hybrid_FW/test data/data.xlsx"

    def test_logging_in(self):

        result_list = []

        self.driver = webdriver.Chrome("C:/Users/Prem/PycharmProjects/page_object_model_1/drivers/chromedriver.exe")
        #self.driver.maximize_window()
        self.driver.get(self.baseurl)
        time.sleep(2)
        self.obj1_login = test_login(self.driver)
        number_of_rows = xlutilities.rownum(self.path,"Sheet1")
        print(number_of_rows)


        for r in range(2,number_of_rows+1):
            self.username = xlutilities.read_data(self.path,"Sheet1",r,1)
            self.password = xlutilities.read_data(self.path, "Sheet1", r, 2)
            self.exp = xlutilities.read_data(self.path, "Sheet1", r, 3)

            self.obj1_login.set_username(self.username)
            time.sleep(3)
            self.obj1_login.set_password(self.password)
            time.sleep(3)
            self.obj1_login.click_login()
            time.sleep(5)

            actual_res = self.driver.title
            exp_res = "Dashboard / nopCommerce administration"
            time.sleep(3)
            if actual_res == exp_res:
                if self.exp == "Logged In":
                    self.obj1_login.click_logout()
                    time.sleep(10)
                    result_list.append("Pass")
                elif self.exp == "Login failed":
                    self.obj1_login.click_logout()
                    time.sleep(10)
                    result_list.append("Fail")
            elif actual_res != exp_res:
                if self.exp == "Logged In":
                    result_list.append("Fail")
                    time.sleep(3)
                elif self.exp == "Login failed":
                    result_list.append("Pass")
                    time.sleep(3)
        print(result_list)

        if "Fail" not in result_list:
            print("This login test is passed")
            self.driver.close()
            assert True
        else:
            print("Login test failed")
            self.driver.close()
            assert False

# Half of the program is running successfully, But remaining half of the program is not running. Need to check later




