import time

class test_login():
    def __init__(self,driver):
        self.driver=driver

        self.username_box_id = "Email"
        self.password_box_id = "Password"
        self.login_button_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
        time.sleep(3)
        self.logout_button_xpath = "/html/body/div[3]/div[1]/div/div/ul/li[3]/a"

    def set_username(self,username):
        self.driver.find_element_by_id(self.username_box_id).clear()
        self.driver.find_element_by_id(self.username_box_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element_by_id(self.password_box_id).clear()
        self.driver.find_element_by_id(self.password_box_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
