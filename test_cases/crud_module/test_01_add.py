import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.add_model import Add_model

@pytest.mark.usefixtures("setup")
class Test_Add():
    def test_add(self):
         lp = LoginPage(self.driver)
         lp.enter_username("robyn.hills@sematree.com")
         lp.enter_password("*Welcome&Tech2022")
         lp.click_login_btn()
         time.sleep(6)
         hp = HomePage(self.driver)  # this is used to sent driver to page
         hp.click_menu_bar()
         time.sleep(3)
         hp.navigate_to("Administration","Categories","Sample Types")
         time.sleep(3)
         hp.click_add_button()
         time.sleep(3)
         add_model = Add_model(self.driver)
         self.input_name = "new sample_add" # is same as for add model
         add_model.add(self.input_name,"added for test","8838yo205")
         time.sleep(5)
         add_model.add_toaster(self.input_name)
         time.sleep(10)


