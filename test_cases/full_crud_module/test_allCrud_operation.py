import time

import pytest

from page.add_model import Add_model
from page.delete_modal import Delete_page
from page.home_page import HomePage
from page.login_page import LoginPage
from page.modify_modal import Modify_page


@pytest.mark.usefixtures("setup")
class Test_AllCrud():
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
          self.input_name = "new sample2"  # is same as for add model
          add_model.name_input(self.input_name)  # data's should be unique and non redundant
          add_model.description_testbox("added for testing")
          add_model.bussiness_code_input("8838yo203")  # data's should be unique and non redundant
          time.sleep(6)
          add_model.submit_btn()
          time.sleep(5)
          add_model.add_toaster(self.input_name)
          time.sleep(8)

     def test_search(self):
         hp = HomePage(self.driver)
         hp.search_input("new sample2")
         time.sleep(3)
         hp.search_button()
         time.sleep(8)

     def test_modify(self):
         hp = HomePage(self.driver)
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
         time.sleep(8)

     def test_delete(self):
         hp = HomePage(self.driver)
         hp.delete_btn()
         time.sleep(5)
         dele_page = Delete_page(self.driver)
         dele_page.delete_confirm()
         time.sleep(5)
         dele_page.delete_toaster()
         time.sleep(8)
