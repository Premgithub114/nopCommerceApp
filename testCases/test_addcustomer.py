from selenium import webdriver
import time
import pytest
import unittest
from pageobjects.add_customer_page import test_add_customer
from pageobjects.login_page import test_login
from Utilities.read_data import all_data
import string
import random

class test_customer_adding(unittest.TestCase):

    baseurl = all_data.get_url()
    user_email = all_data.get_user_email()
    user_password = all_data.get_passw()

    @pytest.mark.sanity
    def test_add_cust(self):
        self.driver = webdriver.Chrome("C:/Users/Prem/PycharmProjects/page_object_model_1/drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        time.sleep(2)
        self.object1 = test_login(self.driver)
        self.object1.set_username(self.user_email)
        self.object1.set_password(self.user_password)
        time.sleep(3)
        self.object1.click_login()
        time.sleep(3)

        self.addcust = test_add_customer(self.driver)
        self.addcust.customer_link()
        time.sleep(2)
        self.addcust.customers_link()
        time.sleep(2)
        self.addcust.add_new_button()
        time.sleep(2)
        #self.email = random_generator + "@gmail.com"
        self.addcust.enter_email("kireeti.prem@gmail.com")
        time.sleep(2)
        self.addcust.enter_password("GBSxyz@123")
        time.sleep(2)
        self.addcust.enter_Firstname("Prem")
        time.sleep(2)
        self.addcust.enter_lastname("Kireeti")
        time.sleep(2)
        self.addcust.select_gender("Male")
        time.sleep(2)
        self.addcust.enter_dob("1/05/1996")
        time.sleep(2)
        self.addcust.enter_companyname("GBS")
        time.sleep(2)
        self.addcust.select_role("Guests")
        time.sleep(2)
        self.addcust.manage_vendor("Vendor 1")
        time.sleep(2)
        self.addcust.admit_comment_text("This is for testing purpose...")
        time.sleep(2)
        self.addcust.save_employee()
        time.sleep(2)

        self.msg = self.driver.find_element_by_tag_name('body').text
        print(self.msg)

        if "customer has been added successfully" in self.msg:
            assert True
        else:
            self.driver.get_screenshot_as_file("C:/Users/Prem/PycharmProjects/Hybrid_FW/screenshots" + "add_cust_screen.png")
            assert False

        self.driver.close()

# For generating a random email address everytime we run the testcase
#def random_generator(size=8,chars = string.ascii_lowercase + string.digits):
 #   return "".join(random.choice(chars) for x in range(size))


