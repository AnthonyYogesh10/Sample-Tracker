import json
import time

import pytest
import requests

from pages.home_page import HomePage
from pages.login_page import LoginPage

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
         new_url = hp.fetch_url()
         print(new_url)
         response = requests.get(new_url)
         status_code = response.status_code
         print(status_code)
         data = response.json()
         print(data)
         time.sleep(2)





