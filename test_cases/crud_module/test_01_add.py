import time
import unittest

import softest
from ddt import ddt,data,file_data,unpack
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.add_model import Add_model
from utilities.utilities import utils

ut = utils()
@pytest.mark.usefixtures("setup")
@ddt
class Test_Add(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
         self.lp = LoginPage(self.driver) # this is used to sent driver to page
         self.hp = HomePage(self.driver)
         self.add_modal = Add_model(self.driver)

    def login(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    def test_01_log(self):
        self.login()

    # @file_data("/home/chris/Desktop/automation/DDT-method/test_data/test_add_data.json")
    # @file_data("/home/chris/Desktop/automation/DDT-method/test_data/test_add_data.yaml")
    @data(*ut.read_data_from_excel("/home/chris/Desktop/automation/DDT-method/test_data/demo_add_data.xlsx","Sheet1"))
    @unpack
    def test_02_add_btn(self,name, description, bussiness_code):
        self.hp.click_add_button()
        self.add_modal.add(name, description, bussiness_code)
        self.add_modal.add_toaster()
