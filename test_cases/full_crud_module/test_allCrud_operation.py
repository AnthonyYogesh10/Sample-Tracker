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
     def test_add(self):
          lp = LoginPage(self.driver)
          lp.enter_username("robyn.hills@sematree.com")
          lp.enter_password("*Welcome&Tech2022")
          lp.click_login_btn()
          time.sleep(7)
          hp = HomePage(self.driver)  # this is used to sent driver to page
          hp.click_menu_bar()
          time.sleep(3)
          hp.select_side_nav("Administration")
          time.sleep(3)
          hp.select_nav_admin_drdw("Categories")
          time.sleep(3)
          hp.select_under_categories("Sample Types")
          time.sleep(8)
          hp.click_add_button()
          time.sleep(3)
          add_model = Add_model(self.driver)
          self.input_name = "new sample2"  # is same as for add model
          add_model.enter_name_input(self.input_name)  # data's should be unique and non redundant
          add_model.enter_description_testbox("added for testing")
          add_model.enter_bussiness_code_input("8838yo203")  # data's should be unique and non redundant
          time.sleep(3)
          add_model.click_submit_btn()
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
         modify_page.enter_name_input("22")
         modify_page.enter_description_testbox("22")
         modify_page.enter_bussiness_code_input("22")
         time.sleep(3)
         modify_page.click_save_btn()
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