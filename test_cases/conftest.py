import time
import pytest

from py.xml import html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
 serv_obj = Service("/home/cb/Downloads/webdrivers/chromedriver")
 driver = webdriver.Chrome(service=serv_obj)
 driver.get("https://intertek-dev.trutesta.io/trusamples.mdb5/samples/cf5c0b49-6f07-4a93-b379-dba01ccde2db/sample-details-tab")
 driver.maximize_window()
 time.sleep(6)
 request.cls.driver = driver
 yield
 driver.close()
