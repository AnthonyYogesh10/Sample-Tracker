import time

from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self,driver):
        self.driver = driver
   #Locators (it is used to change url easily and essy to maintain)
    menubar_field = "//i[@class='fas fa-bars fa-2x']"
    side_nav_options_field = "//ul[@id='scroll-container']/mdb-sidenav-item/li/div/a"
    side_nav_admin_drdw_field = "//ul[@class='sidenav-collapse collapse show']/li"
    under_categories_field = "//mdb-sidenav-item[@class='ng-star-inserted']//li[@class='sidenav-item']/div/a"
    add_button_field = "//button[normalize-space()='Add']"
    modify_btn_field = "//button[normalize-space()='Modify']"
    delete_btn_field = "//button[normalize-space()='Delete']"
    search_input_field = "//input[@id='quick-search']"
    search_button_field = "//i[@class='fa fa-search']"

  # Loactors to Use (It is used to avoid store variables
  #                 eg: name = xpath
  #                     name.click )
    def get_menubar_field(self):
        return self.driver.find_element(By.XPATH,self.menubar_field)
    def get_side_nav_options_field(self):
        return self.driver.find_elements(By.XPATH,self.side_nav_options_field)
    def get_side_nav_admin_drdw_field(self):
        return self.driver.find_elements(By.XPATH,self.side_nav_admin_drdw_field)
    def get_under_categories_field(self):
        return self.driver.find_elements(By.XPATH,self.under_categories_field)
    def get_add_button_field(self):
        return self.driver.find_element(By.XPATH,self.add_button_field)
    def get_modify_btn_field(self):
        return self.driver.find_element(By.XPATH,self.modify_btn_field)
    def get_delete_btn_field(self):
        return self.driver.find_element(By.XPATH,self.delete_btn_field)
    def get_search_input_field(self):
        return self.driver.find_element(By.XPATH,self.search_input_field)
    def get_search_button_field(self):
        return self.driver.find_element(By.XPATH,self.search_button_field)


    def click_menu_bar(self):
        self.get_menubar_field().click()

    def select_side_nav(self,nav_options):
        side_nav = self.get_side_nav_options_field()
        for option in side_nav:
            if option.text == nav_options:
                option.click()

    def select_nav_admin_drdw(self,dropdown_options):
         administration_dropdown = self.get_side_nav_admin_drdw_field()
         for dropdown_option in administration_dropdown: #change it to utlities folder
             if dropdown_option.text == dropdown_options:
                 dropdown_option.click()

    def select_under_categories(self,category_option):
        category_dropdown = self.get_under_categories_field()
        for dropdown in category_dropdown: #change it to utlities folder
            if dropdown.text == category_option:
                dropdown.click()

    def click_add_button(self):
         self.get_add_button_field().click()

    def click_modify_btn(self):
        self.get_modify_btn_field().click()

    def click_delete_btn(self):
        self.get_delete_btn_field().click()

    def enter_search_input(self,search_value):
         self.get_search_input_field().send_keys(search_value)

    def click_search_button(self):
         self.get_search_button_field().click()

    def navigate_to(self,navigate_to,administration,category):
        self.select_side_nav(navigate_to)
        time.sleep(3)
        self.select_nav_admin_drdw(administration)
        time.sleep(3)
        self.select_under_categories(category)

    def fetch_url(self):
        new_url= self.driver.current_url
        return new_url

    def data_of_sample_type(self):
        datas = self.driver.find_elements(By.XPATH,"//div[@id='mid-list']/a")
        lenth_of_data = len(datas)
        # for data in datas:

