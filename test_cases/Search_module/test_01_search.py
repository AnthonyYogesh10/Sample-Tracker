import time

import pytest
from page.home_page import HomePage
from page.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class Test_Search():
    def test_search(self):
         lp = LoginPage(self.driver)
         lp.username("robyn.hills@sematree.com")
         lp.password("*Welcome&Tech2022")
         lp.login_btn()
         time.sleep(6)
         hp = HomePage(self.driver)
         hp.menu_bar()
         time.sleep(3)
         hp.side_nav("Administration")
         time.sleep(3)
         hp.side_nav_admin_drdw("Categories")
         time.sleep(3)
         hp.under_categories("Sample Types")
         time.sleep(3)
         hp.search_input("test")
         time.sleep(3)
         hp.search_button()
         time.sleep(8)



