import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page

@pytest.mark.usefixtures("setup")
class Test_Modify():
    def test_modify(self):
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
         hp.modify_btn()
         time.sleep(3)
         modify_page = Modify_page(self.driver)
         modify_page.name_input("22")
         modify_page.description_testbox("22")
         modify_page.bussiness_code_input("22")
         time.sleep(3)
         modify_page.save_btn()
         time.sleep(6)
         modify_page.modify_toaster()
         time.sleep(6)
