import time
import unittest
import pytest

import softest
from ddt import ddt, data, file_data, unpack

from pages.add_model import Add_model
from pages.delete_modal import Delete_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.modify_modal import Modify_page
from utilities.utilities import utils

ut = utils()


@pytest.mark.usefixtures("setup")
@ddt
class Test_AllCrud(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.add_modal = Add_model(self.driver)
        self.modify_modal = Modify_page(self.driver)
        self.dele_modal = Delete_page(self.driver)

    def login(self):
        self.lp.login("robyn.hills@sematree.com", "*Welcome&Tech2022")
        self.hp.click_menu_bar()
        self.hp.navigate_to("Administration", "Categories", "Sample Types")

    def test_01_log(self):
        self.login()

    @data(*ut.read_data_from_excel("/home/chris/Desktop/automation/Sample-Tracker/test_data/add_data.xlsx", "Sheet1"))
    @unpack
    def test_02_add(self, name, description, bussiness_code):
        self.hp.click_add_button()
        self.add_modal.add(name, description, bussiness_code)
        self.add_modal.add_toaster()

    @data("Sample")
    def test_03_search(self, value):
        self.hp.enter_search_input(value)
        self.hp.click_search_button()

    @data(("sampleTracker_modify", "Modified data", "810Ybecse"))
    @unpack
    def test_04_modify(self, name, description, bussiness_code):
        self.hp.click_modify_btn()
        self.modify_modal.modify(name, description, bussiness_code)
        self.modify_modal.modify_toaster()

    def test_05_delete(self):
        self.hp.click_delete_btn()
        self.dele_modal.click_delete_confirm()
        self.dele_modal.delete_toaster()
