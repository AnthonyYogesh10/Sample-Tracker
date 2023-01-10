from selenium.webdriver.common.by import By


class Add_model():
    def __init__(self,driver):
        self.driver = driver

    def name_input(self,input_value):
        name = self.driver.find_element(By.XPATH,"//input[@id='shipment-type-name']")
        name.clear()
        name.send_keys(input_value)

    def description_testbox(self,description_value):
        description = self.driver.find_element(By.XPATH,"//textarea[@id='shipment-type-description']")
        description.clear()
        description.send_keys(description_value)

    def bussiness_code_input(self,input_value):
        bussiness_code = self.driver.find_element(By.XPATH,"//input[@id='businessCode']")
        bussiness_code.clear()
        bussiness_code.send_keys(input_value)

    def item_status_inactive(self):
        item_status = self.driver.find_element(By.XPATH,"//input[@id='deliverable-item-status']")
        item_status.click()

    def submit_btn(self):
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/mdb-modal-container[1]/div[1]/div[1]/add-shipment-type-modal[1]/div[3]/button[1]").click()

    def add_toaster(self,input_name):
        success_value=self.driver.find_element(By.XPATH,"//div[@class='toast-body bg-light']").text
        # print(success_value)
        s1 = input_name
        s2 = " Is Added"
        s3 = s1 + s2
        print(s3)
        # print(success_value)
        #to verify the heading is equal to input value
        heading = self.driver.find_element(By.XPATH,"//span[normalize-space()='new sample2']")
        heading_text = heading.text
        if success_value == s3 and heading_text == input_name:
           print("testcase add passed")
        else:
            assert "testcase add failed"

    def cancel_btn(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']").click()
