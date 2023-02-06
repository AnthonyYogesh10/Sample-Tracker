import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.delete_modal import Delete_page

@pytest.mark.usefixtures("setup")
class Test_Delete():
    def test_delete(self):
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
         hp.click_delete_btn()
         time.sleep(5)
         dele_page = Delete_page(self.driver)
         dele_page.click_delete_confirm()
         time.sleep(5)
         dele_page.delete_toaster()
         time.sleep(5)
