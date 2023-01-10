import time

import pytest
from Sample_tracker.page.home_page import HomePage
from Sample_tracker.page.login_page import LoginPage
from Sample_tracker.page.add_model import Add_model

@pytest.mark.usefixtures("setup")
class Test_Add():
    def test_add(self):
         lp = LoginPage(self.driver)
         lp.username("robyn.hills@sematree.com")
         lp.password("*Welcome&Tech2022")
         lp.login_btn()
         time.sleep(6)
         hp = HomePage(self.driver)  # this is used to sent driver to page
         hp.menu_bar()
         time.sleep(3)
         hp.side_nav("Administration")
         time.sleep(3)
         hp.side_nav_admin_drdw("Categories")
         time.sleep(3)
         hp.under_categories("Sample Types")
         time.sleep(3)
         hp.add_button()
         time.sleep(3)
         add_model = Add_model(self.driver)
         self.input_name = "new sample2" # is same as for add model
         add_model.name_input(self.input_name) #data's should be unique and non redundant
         add_model.description_testbox("added for testing")
         add_model.bussiness_code_input("8838yo203")#data's should be unique and non redundant
         time.sleep(6)
         add_model.submit_btn()
         time.sleep(5)
         add_model.add_toaster(self.input_name)
         time.sleep(10)


