import time

from selenium.webdriver.common.by import By
from utilities.utilities import utils
class Delete_page():
    log = utils().custom_logger(mode='a')
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

    def click_delete_confirm(self):
        self.get_delete_confirm_field().click()
        self.log.info("Click on confirm button")
        time.sleep(5)
    def click_delete_cancel(self):
        self.get_delete_cancel_field().click()
        self.log.info("Click on cancel button")

    def delete_toaster(self):
        toaster = self.get_delete_toaster_succ_field()
        toaste_text = toaster.text
        print(toaste_text)
        if toaste_text == "Success":
            self.log.info("testcase delete passed")
        else:
            self.log.info("testcase delete failed")
    time.sleep(6)
