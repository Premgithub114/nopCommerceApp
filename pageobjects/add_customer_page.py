from selenium.webdriver.support.ui import Select
import time

class test_add_customer:
    customer_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    customers_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    add_new_xpath = "/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a"
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    firstname_textbox_id = "FirstName"
    lastname_textbox_id = "LastName"
    male_gender_radio_id = "Gender_Male"
    female_gender_radio_id = "Gender_Female"
    dob_textbox_id = "DateOfBirth"
    company_name_id = "Company"
    is_tax_textbox_id = "IsTaxExempt"
    delete_role = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    customer_roles_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    administrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    forum_moderators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    guests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    vendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    manage_vendor_xpath = "//*[@id='VendorId']"
    no_vendor_xpath = "//*[@id='VendorId']/option[1]"
    vendor1_xpath = "//*[@id='VendorId]/option[2]"
    vendor2_xpath = "//*[@id='VendorId']/option[3]"
    active_id = "Active"
    admin_comment_id = "AdminComment"
    save_button_xpath = "/html/body/div[3]/div[3]/div/form/div[1]/div/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def customer_link(self):
        self.driver.find_element_by_xpath(self.customer_xpath).click()

    def customers_link(self):
        self.driver.find_element_by_xpath(self.customers_xpath).click()

    def add_new_button(self):
        self.driver.find_element_by_xpath(self.add_new_xpath).click()

    def enter_email(self,email):
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def enter_Firstname(self,firstname):
        self.driver.find_element_by_id(self.firstname_textbox_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element_by_id(self.lastname_textbox_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_id(self.male_gender_radio_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.female_gender_radio_id).click()
        else:
            self.driver.find_element_by_id(self.male_gender_radio_id).click()

    def enter_dob(self,dob):
        self.driver.find_element_by_id(self.dob_textbox_id).send_keys(dob)

    def enter_companyname(self,company):
        self.driver.find_element_by_id(self.company_name_id).send_keys(company)

    def is_tax(self):
        self.driver.find_element_by_id(self.is_tax_textbox_id).click()

    def select_role(self,role):
        self.driver.find_element_by_xpath(self.customer_roles_xpath).click()
        time.sleep(5)

        if role == 'Administrator':
            self.item = self.driver.find_element_by_xpath(self.administrators_xpath)
        elif role == 'Forum moderator':
            self.item = self.driver.find_element_by_xpath(self.forum_moderators_xpath)
        elif role == 'Guests':
            self.driver.find_element_by_xpath(self.delete_role).click()
            self.item = self.driver.find_element_by_xpath(self.guests_xpath)
        elif role == 'Vendor':
            self.item = self.driver.find_element_by_xpath(self.vendors_xpath)
        else:
            self.item = self.driver.find_element_by_xpath(self.guests_xpath)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click()",self.item)

    def manage_vendor(self,vendor_name):
        drp = Select(self.driver.find_element_by_xpath(self.manage_vendor_xpath))
        drp.select_by_visible_text(vendor_name)

    def active_checkbox(self):
        self.driver.find_element_by_id(self.active_id).click()

    def admit_comment_text(self,text):
        self.driver.find_element_by_id(self.admin_comment_id).send_keys(text)

    def save_employee(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
