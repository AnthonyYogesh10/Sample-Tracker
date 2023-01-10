import time

import pytest
from Sample_tracker.page.home_page import HomePage
from Sample_tracker.page.login_page import LoginPage
from Sample_tracker.page.delete_modal import Delete_page

@pytest.mark.usefixtures("setup")
class Test_Delete():
    def test_delete(self):
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
         hp.delete_btn()
         time.sleep(5)
         dele_page = Delete_page(self.driver)
         dele_page.delete_confirm()
         time.sleep(5)
         dele_page.delete_toaster()
         time.sleep(5)
