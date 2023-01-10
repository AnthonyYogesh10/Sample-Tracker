from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self,driver):
        self.driver = driver

    def menu_bar(self):
        menubar =self.driver.find_element(By.XPATH,"//i[@class='fas fa-bars fa-2x']")
        menubar.click()

    def side_nav(self,nav_options):
        side_nav =self.driver.find_elements(By.XPATH,"//ul[@id='scroll-container']/mdb-sidenav-item/li/div/a")
        for option in side_nav:
            if option.text == nav_options:
                option.click()

    def side_nav_admin_drdw(self,dropdown_options):
         administration_dropdown = self.driver.find_elements(By.XPATH,"//ul[@class='sidenav-collapse collapse show']/li")
         for dropdown_option in administration_dropdown:
             if dropdown_option.text == dropdown_options:
                 dropdown_option.click()

    def under_categories(self,category_option):
        category_dropdown = self.driver.find_elements(By.XPATH,"//mdb-sidenav-item[@class='ng-star-inserted']//li[@class='sidenav-item']/div/a")
        for dropdown in category_dropdown:
            if dropdown.text == category_option:
                dropdown.click()

    def add_button(self):
         add =self.driver.find_element(By.XPATH,"//button[normalize-space()='Add']")
         add.click()

    def data_of_sample_type(self):
        datas = self.driver.find_elements(By.XPATH,"//div[@id='mid-list']/a")
        lenth_of_data = len(datas)
        # for data in datas:

    def modify_btn(self):
        modify = self.driver.find_element(By.XPATH,"//button[normalize-space()='Modify']")
        modify.click()

    def delete_btn(self):
        delete = self.driver.find_element(By.XPATH,"//button[normalize-space()='Delete']")
        delete.click()

    def search_input(self,search_value):
        search = self.driver.find_element(By.XPATH,"//input[@id='quick-search']")
        search.send_keys(search_value)

    def search_button(self):
        search_btn = self.driver.find_element(By.XPATH,"//i[@class='fa fa-search']")
        search_btn.click()



