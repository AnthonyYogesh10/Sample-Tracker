import time

import pytest

from pages.add_model import  Add_model
from pages.delete_modal import Delete_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page
from pytest_html import extras

@pytest.mark.usefixtures("setup")
class Test_AllCrud():
     def test_login(self):
          lp = LoginPage(self.driver)
          lp.login("robyn.hills@sematree.com","*Welcome&Tech2022")
          time.sleep(7)

     def test_navigate(self):
          hp = HomePage(self.driver)  # this is used to sent driver to page
          hp.click_menu_bar()
          time.sleep(3)
          hp.navigate_to("Administration","Categories","Sample Types")
          time.sleep(8)
          hp.click_add_button()
          time.sleep(3)

     def test_add(self):
          add_model = Add_model(self.driver)
          self.input_name = "new sample2"  # is same as for add model
          add_model.add(self.input_name,"added for testing","8838yo203")
          time.sleep(5)
          add_model.add_toaster(self.input_name)
          time.sleep(6)

     def test_search(self):
         hp = HomePage(self.driver)
         time.sleep(2)
         hp.enter_search_input("new sample2")
         time.sleep(3)
         hp.click_search_button()
         time.sleep(3)

     def test_modify(self):
         hp = HomePage(self.driver)
         hp.click_modify_btn()
         time.sleep(5)
         modify_page = Modify_page(self.driver)
         modify_page.modify("22","22","22")
         time.sleep(6)
         modify_page.modify_toaster()
         time.sleep(6)

     def test_delete(self):
         hp = HomePage(self.driver)
         hp.click_delete_btn()
         time.sleep(3)
         dele_page = Delete_page(self.driver)
         dele_page.click_delete_confirm()
         time.sleep(5)
         dele_page.delete_toaster()
         time.sleep(6)

     # def test_extra(extra):
     #     extra.append(extras.text("some string"))