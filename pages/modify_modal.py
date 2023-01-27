import time

from selenium.webdriver.common.by import By

class Modify_page():
    def __init__(self,driver):
        self.driver = driver

    name_input_field = "//input[@id='shipmentType-name']"
    description_testbox_field = "//textarea[@id='description']"
    bussiness_code_input_field = "//input[@id='shipmentType-businessCode']"
    item_status_inactive_field = "//input[@id='openOnly']"
    save_btn_field = "//button[@type='submit']"
    cancel_btn_field = "//button[normalize-space()='Cancel']"
    modify_toaster_field = "//strong[@class='me-auto text-dark']"

    def get_name_input_field(self):
        return self.driver.find_element(By.XPATH,self.name_input_field)
    def get_description_testbox_field(self):
        return self.driver.find_element(By.XPATH,self.description_testbox_field)
    def get_bussiness_code_input_field(self):
        return self.driver.find_element(By.XPATH,self.bussiness_code_input_field)
    def get_item_status_inactive_field(self):
        return self.driver.find_element(By.XPATH,self.item_status_inactive_field)
    def get_save_btn_field(self):
        return self.driver.find_element(By.XPATH,self.save_btn_field)
    def get_cancel_btn_field(self):
        return self.driver.find_element(By.XPATH,self.cancel_btn_field)
    def get_modify_toaster_field(self):
        return self.driver.find_element(By.XPATH,self.modify_toaster_field)

    def enter_name_input(self,input_value):
        self.get_name_input_field().send_keys(input_value)

    def enter_description_testbox(self,description_value):
        self.get_description_testbox_field().send_keys(description_value)

    def enter_bussiness_code_input(self,input_value):
        self.get_bussiness_code_input_field().send_keys(input_value)

    def click_item_status_inactive(self):
        self.get_item_status_inactive_field().click()

    def click_save_btn(self):
        self.get_save_btn_field().click()

    def click_cancel_btn(self):
       self.get_cancel_btn_field().click()

    def modify_toaster(self,):
        toaster = self.get_modify_toaster_field()
        toaster_text = toaster.text
        print(toaster_text)
        if toaster_text == "Success":
            print("testcase modify passed")
        else:
            print("testcase modify failed")

    def modify(self,name,description,bussiness_code):
        self.enter_name_input(name)
        self.enter_description_testbox(description)
        self.enter_bussiness_code_input(bussiness_code)
        time.sleep(3)
        self.click_save_btn()
