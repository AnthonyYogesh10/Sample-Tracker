from selenium.webdriver.common.by import By


class Add_model():
    def __init__(self, driver):
        self.driver = driver

    name_input_field = "//input[@id='shipment-type-name']"
    description_testbox_field = "//textarea[@id='shipment-type-description']"
    bussiness_code_input_field = "//input[@id='businessCode']"
    item_status_inactive_field = "//input[@id='deliverable-item-status']"
    submit_btn_field = "//body[1]/div[1]/div[2]/div[1]/mdb-modal-container[1]/div[1]/div[1]/add-shipment-type-modal[1]/div[3]/button[1]"
    add_toaster_field = "//div[@class='toast-body bg-light']"
    cancel_btn_field = "//button[normalize-space()='Cancel']"

    def get_name_input_field(self):
        return self.driver.find_element(By.XPATH, self.name_input_field)

    def get_description_field(self):
        return self.driver.find_element(By.XPATH, self.description_testbox_field)

    def get_bussiness_code_input_field(self):
        return self.driver.find_element(By.XPATH, self.bussiness_code_input_field)

    def get_item_status_inactive_field(self):
        return self.driver.find_element(By.XPATH, self.item_status_inactive_field)

    def get_submit_btn_field(self):
        return self.driver.find_element(By.XPATH, self.submit_btn_field)

    def get_add_toaster_field(self):
        return self.driver.find_element(By.XPATH, self.add_toaster_field)

    def get_cancel_btn_field(self):
        return self.driver.find_element(By.XPATH, self.cancel_btn_field)

    def enter_name_input(self, input_value):
        self.get_name_input_field().clear()
        self.get_name_input_field().send_keys(input_value)

    def enter_description_testbox(self, description_value):
        self.get_description_field().clear()
        self.get_description_field().send_keys(description_value)

    def enter_bussiness_code_input(self, input_value):
        self.get_bussiness_code_input_field().clear()
        self.get_bussiness_code_input_field().send_keys(input_value)

    def click_item_status_inactive(self):
        self.get_item_status_inactive_field().click()

    def click_submit_btn(self):
        self.get_submit_btn_field().click()

    def click_cancel_btn(self):
        self.get_cancel_btn_field().click()

    def add_toaster(self, input_name):
        success_value = self.get_add_toaster_field().text
        # print(success_value)
        s1 = input_name
        s2 = " Is Added"
        s3 = s1 + s2
        print(s3)
        # print(success_value)
        # to verify the heading is equal to input value
        heading = self.driver.find_element(By.XPATH, "//span[normalize-space()='new sample2']")
        heading_text = heading.text
        if success_value == s3 and heading_text == input_name:
            print("testcase add passed")
        else:
                assert "testcase add failed"




