from selenium.webdriver.common.by import By

class LoginPage():
 def __init__(self,driver):
     self.driver = driver

 def username(self,username_value):
     username_input = self.driver.find_element(By.ID,"username")
     username_input.send_keys(username_value)

 def password(self,password_value):
     password_input = self.driver.find_element(By.ID,"password")
     password_input.send_keys(password_value)

 def login_btn(self):
     login_btn= self.driver.find_element(By.ID,"kc-login")
     login_btn.click()

