from selenium.webdriver.common.by import By

class Delete_page():
    def __init__(self,driver):
        self.driver = driver

    def delete_confirm(self):
        delete =self.driver.find_element(By.XPATH,"//button[normalize-space()='Confirm']")
        delete.click()

    def delete_toaster(self):
        toaster = self.driver.find_element(By.XPATH,"//div[@class='toast-header bg-light']")
        toaste_text = toaster.text
        print(toaste_text)
        if toaste_text == "Success":
            print("testcase delete passed")
        else:
            print("testcase delete failed")

    def delete_cancel(self):
        cancel = self.driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']")
        cancel.click()