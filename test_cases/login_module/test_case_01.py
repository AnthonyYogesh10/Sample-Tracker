import time
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
@pytest.mark.usefixtures("setup")
class TestCredential():
   def test_login(self):
     lp = LoginPage(self.driver) # this is used to sent driver to page
     lp.enter_username("robyn.hills@sematree.com")
     lp.enter_password("*Welcome&Tech2022")
     lp.click_login_btn()
     time.sleep(6)
     hp = HomePage(self.driver) # this is used to sent driver to page
     hp.click_menu_bar()

