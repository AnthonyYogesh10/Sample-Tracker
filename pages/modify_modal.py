from selenium.webdriver.common.by import By

class Modify_page():
    def __init__(self,driver):
        self.driver = driver

    def name_input(self,input_value):
        name = self.driver.find_element(By.XPATH,"//input[@id='shipmentType-name']")
        name.send_keys(input_value)

    def description_testbox(self,description_value):
        description = self.driver.find_element(By.XPATH,"//textarea[@id='description']")
        description.send_keys(description_value)

    def bussiness_code_input(self,input_value):
        bussiness_code = self.driver.find_element(By.XPATH,"//input[@id='shipmentType-businessCode']")
        bussiness_code.send_keys(input_value)

    def item_status_inactive(self):
        item_status = self.driver.find_element(By.XPATH,"//input[@id='openOnly']")
        item_status.click()

    def save_btn(self):
        save = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        save.click()

    def modify_toaster(self,):
        toaster = self.driver.find_element(By.XPATH,"//strong[@class='me-auto text-dark']")
        toaster_text = toaster.text
        print(toaster_text)
        if toaster_text == "Success":
            print("testcase modify passed")
        else:
            print("testcase modify failed")

    def cancel_btn(self):
        cancel = self.driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']")
        cancel.click()


