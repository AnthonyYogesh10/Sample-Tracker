import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page

@pytest.mark.usefixtures("setup")
class Test_Modify():
    def test_modify(self):
         lp = LoginPage(self.driver)
         lp.enter_username("robyn.hills@sematree.com")
         lp.enter_password("*Welcome&Tech2022")
         lp.click_login_btn()
         time.sleep(6)
         hp = HomePage(self.driver)  # this is used to sent driver to page
         hp.click_menu_bar()
         time.sleep(3)
         hp.navigate_to("Administration","Categories","Sample Types")
         time.sleep(5)
         hp.click_modify_btn()
         time.sleep(3)
         modify_page = Modify_page(self.driver)
         modify_page.modify("22","22","22")
         time.sleep(6)
         modify_page.modify_toaster()
         time.sleep(6)
