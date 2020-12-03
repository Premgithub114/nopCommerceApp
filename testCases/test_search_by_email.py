from selenium import webdriver
import time
import pytest
import unittest
from pageobjects.add_customer_page import test_add_customer
from pageobjects.login_page import test_login
from Utilities.read_data import all_data
from pageobjects.search_with_email_and_name import search_elements

class test_searching_customer(unittest.TestCase):

    baseurl = all_data.get_url()
    user_email = all_data.get_user_email()
    user_password = all_data.get_passw()
    @pytest.mark.regression
    def test_search_cust(self):
        self.driver = webdriver.Chrome("C:/Users/Prem/PycharmProjects/page_object_model_1/drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        time.sleep(2)
        self.object2 = test_login(self.driver)
        self.object2.set_username(self.user_email)
        self.object2.set_password(self.user_password)
        time.sleep(3)
        self.object2.click_login()
        time.sleep(3)

        self.addcust = test_add_customer(self.driver)
        self.addcust.customer_link()
        time.sleep(2)
        self.addcust.customers_link()
        time.sleep(2)

        self.search_cus = search_elements(self.driver)
        self.search_cus.enter_email("james_pan@nopCommerce.com")
        time.sleep(2)
        self.search_cus.search_button()
        time.sleep(5)
        status = self.search_cus.search_by_email("james_pan@nopCommerce.com")
        assert status


