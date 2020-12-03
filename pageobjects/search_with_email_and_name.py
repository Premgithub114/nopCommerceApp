from selenium import webdriver

class search_elements:
    email_search_id = "SearchEmail"
    first_name_id = "SearchFirstName"
    last_name_id = "SearchLastName"
    search_button_id = "search-customers"

    table_xpath = "//*[@id='customers-grid']"  # table without header part
    row_xpath = "//*[@id='customers-grid']/tbody/tr"    # all rows in a table
    col_xpath = "//*[@id='customers-grid']/tbody/tr/td" # all columns in a table

    def __init__(self,driver):
        self.driver= driver

    def enter_email(self,email):
        self.driver.find_element_by_id(self.email_search_id).clear()
        self.driver.find_element_by_id(self.email_search_id).send_keys(email)
    def enter_FN(self,First):
        self.driver.find_element_by_id(self.first_name_id).clear()
        self.driver.find_element_by_id(self.first_name_id).send_keys(First)
    def enter_LN(self,Last):
        self.driver.find_element_by_id(self.last_name_id).clear()
        self.driver.find_element_by_id(self.last_name_id).send_keys(Last)
    def search_button(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def row_count(self):
        return len(self.driver.find_elements_by_xpath(self.row_xpath))

    def col_count(self):
        return len(self.driver.find_element_by_xpath(self.col_xpath))

    def search_by_email(self,email):
        count = False
        table = self.driver.find_element_by_xpath(self.table_xpath)
        for r in range(1,self.row_count()+1):

            email_id = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                count = True
                break
        return count

    def search_by_name(self,name):
        res = False
        table = self.driver.find_element_by_xpath(self.table_xpath)
        for r in range(1,self.row_count()+1):

            full_name = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if full_name == name:
                res = True
                break
        return res


