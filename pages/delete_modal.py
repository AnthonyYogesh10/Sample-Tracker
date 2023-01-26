from selenium.webdriver.common.by import By

class Delete_page():
    def __init__(self,driver):
        self.driver = driver
    delete_confirm_field = "//button[normalize-space()='Confirm']"
    delete_cancel_field = "//button[normalize-space()='Cancel']"
    delete_toaster_succ_field = "//div[@class='toast-header bg-light']"
    def get_delete_confirm_field(self):
        return self.driver.find_element(By.XPATH,self.delete_confirm_field)
    def get_delete_cancel_field(self):
        return self.driver.find_element(By.XPATH,self.delete_confirm_field)
    def  get_delete_toaster_succ_field(self):
        return self.driver.find_element(By.XPATH,self.delete_toaster_succ_field)

    def delete_confirm(self):
        self.get_delete_confirm_field().click()
    def delete_cancel(self):
        self.get_delete_cancel_field().click()

    def delete_toaster(self):
        toaster = self.get_delete_toaster_succ_field()
        toaste_text = toaster.text
        print(toaste_text)
        if toaste_text == "Success":
            print("testcase delete passed")
        else:
            print("testcase delete failed")