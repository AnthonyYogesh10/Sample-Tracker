from selenium.webdriver.common.by import By

class LoginPage():
  def __init__(self,driver):
     self.driver = driver

  username_field = "username" # id selector
  password_field = "password" # id selector
  login_btn_field = "kc-login" # id selector
  def get_username_field(self):
      return self.driver.find_element(By.ID,self.username_field)
  def get_password_field(self):
      return self.driver.find_element(By.ID,self.password_field)
  def get_login_btn_field(self):
      return  self.driver.find_element(By.ID,self.login_btn_field)
  def enter_username(self,username_value):
       self.get_username_field().send_keys(username_value)

  def enter_password(self,password_value):
      self.get_password_field().send_keys(password_value)

  def click_login_btn(self):
      self.get_login_btn_field().click()

  def login(self,username,password):
      self.enter_username(username)
      self.enter_password(password)
      self.click_login_btn()

