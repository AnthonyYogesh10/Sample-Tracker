import os
import time
import pytest

from py.xml import html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pytest_html import extras

@pytest.fixture(scope="class")
def setup(request):
 global driver
 serv_obj = Service("/home/cb/Downloads/webdrivers/chromedriver")
 driver = webdriver.Chrome(service=serv_obj)
 driver.get("https://intertek-dev.trutesta.io/trusamples.mdb5/samples/cf5c0b49-6f07-4a93-b379-dba01ccde2db/sample-details-tab")
 driver.maximize_window()
 time.sleep(6)
 request.cls.driver = driver
 yield
 driver.close()

 def pytest_html_results_table_header(cells):
     # del cells[1]
     # del cells[2]
     cells.insert(0, html.th("S.no"))
     cells.insert(1, html.th("Action"))
     cells.insert(2, html.th("Expected output"))
     cells.insert(3, html.th("Actual output"))
     cells.pop()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://keycloak-gbs-dev.trutesta.io/auth/realms/Intertek/protocol/openid-connect/auth?client_id=trutesta&redirect_uri=https%3A%2F%2Fintertek-dev.trutesta.io%2Ftrusamples.mdb5%2Fshipment-types%2Fb1eccf7f-ae34-4477-85d9-eee1aa138dae%2FshipmentDetails&state=48c7d42d-57c8-4b2d-ba42-634f981935d8&response_mode=fragment&response_type=code&scope=openid&nonce=23743122-f53b-4602-9d51-bcd151a2c6ad"))
#         xfail = hasattr(report, "wasxfail")
#         if(report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = str(int(round(time.time() * 1000))) + ".png"
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             time.sleep(1)
#             driver.save_screenshot(destinationFile)
#             html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
#                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
#             if file_name:
#              extra.append(pytest_html.extras.html(html))
#         report.extra = extra

def pytest_html_report_title(report):
    report.title = "Truetesta Sample Tracker Report"

# def pytest_html_results_table_header(cells):
#     # del cells[1]
#     # del cells[2]
#     cells.insert(0, html.th("S.no"))
#     cells.insert(1, html.th("Action"))
#     cells.insert(2, html.th("Expected output"))
#     cells.insert(3, html.th("Actual output"))
#     cells.pop()

# def pytest_html_results_table_row(report, cells):
#     del cells[1]
#     del cells[2]
#     cells.insert(0, html.td(report.serial_no))
#     cells.insert(1, html.td(report.action))
#     cells.insert(2, html.td(report.expected_output))
#     cells.insert(3, html.td(report.actual_output))
#     cells.pop()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item,call):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     report.serial_no = 10
#     report.action = (["click the search button and use filter to get data"])
#     report.actual_output = (["as per filter data are collected"])
#     report.expected_output ="all data are collected"








