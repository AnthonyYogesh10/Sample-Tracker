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
     @pytest.fixture(autouse=True)
     def class_setup(self):
       self.lp = LoginPage(self.driver)
       self.hp = HomePage(self.driver)
       self.add_model = Add_model(self.driver)
       self.modify_modal = Modify_page(self.driver)
       self.dele_modal = Delete_page(self.driver)

     def test_login(self):
          self.lp.login("robyn.hills@sematree.com","*Welcome&Tech2022")
          time.sleep(7)

     def test_navigate(self):
          self.hp.click_menu_bar()
          time.sleep(3)
          self.hp.navigate_to("Administration","Categories","Sample Types")
          time.sleep(8)
          self.hp.click_add_button()
          time.sleep(3)

     def test_add(self):
          self.input_name = "new sample2"  # is same as for add model
          self.add_model.add(self.input_name,"added for testing","8838yo203")
          time.sleep(5)
          self.add_model.add_toaster(self.input_name)
          time.sleep(6)

     def test_search(self):
         time.sleep(2)
         self.hp.enter_search_input("new sample2")
         time.sleep(3)
         self.hp.click_search_button()
         time.sleep(3)

     def test_modify(self):
         self.hp.click_modify_btn()
         time.sleep(5)
         self.modify_modal.modify("22","22","22")
         time.sleep(6)
         self.modify_modal.modify_toaster()
         time.sleep(6)

     def test_delete(self):
         self.hp.click_delete_btn()
         time.sleep(3)
         self.dele_modal.click_delete_confirm()
         time.sleep(5)
         self.dele_modal.delete_toaster()
         time.sleep(6)

     # def test_extra(extra):
     #     extra.append(extras.text("some string"))