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
         lp.enter_username("robyn.hills@sematree.com")
         lp.enter_password("*Welcome&Tech2022")
         lp.click_login_btn()
         time.sleep(6)
         hp = HomePage(self.driver)
         hp.click_menu_bar()
         time.sleep(3)
         hp.select_side_nav("Administration")
         time.sleep(3)
         hp.select_nav_admin_drdw("Categories")
         time.sleep(3)
         hp.select_under_categories("Sample Types")
         time.sleep(3)
         hp.enter_search_input("test")
         time.sleep(3)
         hp.click_search_button()
         time.sleep(8)
         new_url = "https://devops2.intigna.io/st-sample-tracker-service/sampletracker/admin/shipment-types/794265e6-3858-492d-9f81-d2b47f4f9e9f"
         print(new_url)
         # headers = {
         #      "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3bGdZX0VpZzlpZFFWY3RpeG12QWdvc0RNXzVpVHY0ZWRvWmdYZEFJd1RVIn0.eyJleHAiOjE2NzQxMjU0MjYsImlhdCI6MTY3NDEyNTEyNiwiYXV0aF90aW1lIjoxNjc0MTI1MTI1LCJqdGkiOiIxMTc3NDQxNS1jYTlkLTQwYzktYWJjYi00NzNhMDlhNTZjNWEiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLWdicy1kZXYudHJ1dGVzdGEuaW8vYXV0aC9yZWFsbXMvSW50ZXJ0ZWsiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMDdlMTdjYzgtMGI3Yy00OGU1LThmNGMtOTQ4Y2E3ZTRlNzZjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidHJ1dGVzdGEiLCJub25jZSI6ImQ0MTk0YTM4LTUyYTMtNGU5MC04YWI5LTU2OTE4YzU0ODRhNiIsInNlc3Npb25fc3RhdGUiOiIyYzIwNGY2MC1jMmE1LTQxMTItOTM2NC03M2UwZTc3NjhjZjQiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVzb3VyY2VfYWNjZXNzIjp7InRydXRlc3RhIjp7InJvbGVzIjpbInRydXRlc3RhLWFwcGxpY2F0aW9uLW1vbml0b3JpbmciLCJkZWxpdmVyeUNsaWVudEFjdGlvbnMiLCJ0cnV0ZXN0YS1vcmdhbml6YXRpb25zIiwidHJ1dGVzdGEtYWhhbS1kbHAiLCJzdGFuZGFyZHNVc2VyIiwiZGVsaXZlcnlFc3RpbWF0ZXMiLCJzY2hlZHVsZUZvcmVjYXN0cyIsInNjaGVkdWxlVmlld05vdGlmaWNhdGlvbnMiLCJ0cnV0ZXN0YS1kZWxpdmVyYWJsZXMtYWR2LXF1ZXJ5IiwidHJ1dGVzdGEtYWRtaW4iLCJkZWxpdmVyeURvY3VtZW50cyIsImNsaWVudERlbGl2ZXJhYmxlTG9ja0ludGVncmF0aW9uIiwidHJ1RGVsaXZlcnlDYW5VcGRhdGVQQ0QiLCJ0cnV0ZXN0YS1hY2NvdW50cyIsInNjaGVkdWxlTWFuYWdlVGltZXNoZWV0cyIsInRydWRvY3MtY2FuLW92ZXJyaWRlLXZhbGlkYXRpb24iLCJ0cnV0ZXN0YS1kZWxpdmVyYWJsZXMtbWFuYWdlLWxvY2tzIiwidHJ1dGVzdGFQb3J0YWxVc2VyIiwic2NoZWR1bGVNYW5hZ2VBY3Rpdml0aWVzIiwiZGVsaXZlcnlEZWxpdmVyYWJsZXMiLCJtYXJrRXhlbXB0RnJvbVRlc3RpbmdBY3Rpb24iLCJ0cnV0ZXN0YS1kZWxpdmVyYWJsZXMtc3VuIiwidHJ1dGVzdGEtcG9ydGFsIiwidHJ1dGVzdGEtc3RhbmRhcmRzIiwidHJ1dGVzdGEtdXNlci1pbnNwZWN0b3IiLCJyZXF1ZXN0LWFkbWluIiwiZGVsaXZlcnlFcXVpcG1lbnRMb2ciLCJ0cnVTY2hlZHVsaW5nQ2FuRGVsZXRlQWxsQWN0aXZpdGllcyIsInRydXRlc3RhLWRlbGl2ZXJhYmxlLWFkbWluIiwidHJ1dGVzdGEtZGVsaXZlcnktbWFuYWdlLXJldmlld3MiLCJ0cnV0ZXN0YS1jbGllbnQtZGVsaXZlcmFibGVzIiwidHJ1U2NoZWR1bGluZ0NhbkVkaXRSZXZlbnVlIiwic2NoZWR1bGVEb2N1bWVudHMiLCJ0cnVEZWxpdmVyeUFjdGl2aXR5QXNzaWduIiwicmVxdWVzdENhbkFwcHJvdmVDbGllbnRBY3Rpb24iLCJ0cnV0ZXN0YS1zYW1wbGV0cmFja2VyIiwiY29tcG9uZW50cyIsInRydVNjaGVkdWxpbmdDYW5EcmFnVGFncyIsInRydXRlc3RhLXJlcG9ydC1pbnNwZWN0b3IiLCJ0cnVEZWxpdmVyeUFjdGl2aXR5RGVsZXRlIiwidHJ1RGVsaXZlcnlDYW5Nb2RpZnlBY3Rpdml0eSIsInRydVNjaGVkdWxpbmdDYW5WaWV3UmVzb3VyY2VJbmZvIiwiU2VhcmNoU2VsZWN0aW9ucyIsInNjaGVkdWxlQWN0aXZpdGllcyIsInRydURlbGl2ZXJ5QWN0aXZpdHlDbG9uZSIsImRpcmVjdG9yeVVzZXIiLCJ0cnV0ZXN0YS11c2Vycy1tZXNzYWdpbmciLCJjbGllbnRSZXF1ZXN0QXBwcm92ZXIiLCJ0cnVEZWxpdmVyeUNhbkFkZEFjdGl2aXR5IiwidHJ1RGVsaXZlcnlDb250YWN0QWRkIiwiZW1haWxTZWxlY3Rpb25Ob3RpY2VzIiwidHJ1dGVzdGEtb3JnYW5pemF0aW9uLWFkZCIsInRydXRlc3RhLXJlc291cmNlcyIsInRydURlbGl2ZXJ5Vmlld1Bvb2xzIiwidWxjQ29ycmVzcG9uZGVuY2VRdWV1ZXMiLCJ0cnV0ZXN0YS1lc3RpbWF0ZXMiLCJvcmdhbml6YXRpb25Vc2VyIiwidHJ1dGVzdGEtY29udGFjdC1hZGQiLCJ0cnVTY2hlZHVsaW5nQ2FuRGVsZXRlU2NoZWR1bGUiLCJ0cnV0ZXN0YS1kZWxpdmVyYWJsZXMtaG9sZCIsInRydXRlc3RhLWRhc2hib2FyZCIsInRydVNjaGVkdWxpbmdDYWxlbmRhclRhYmxlVmlldyIsImRlbGl2ZXJ5VXNlciIsInRydXRlc3RhLWRlbGl2ZXJ5LXJldmlldy1zdGF0cyIsInRydXRlc3RhLWF1ZGl0IiwibWFya1NlbGVjdGlvbnNTZW50IiwicHJvamVjdFVzZXIiLCJ0cnV0ZXN0YS1leHRlcm5hbC1hdWRpdHMiLCJTZWFyY2hOb3RpZmljYXRpb25zIiwidHJ1c2NoZWR1bGluZyIsInRydWNvbXBvbmVudHNSZW1pbmRlcnMiLCJ0cnVTY2hlZHVsaW5nQ2FuRWRpdEFjdGl2aXR5TmFtZSIsInRydVNjaGVkdWxpbmdDYW5NYW5hZ2VVcGRhdGVzIiwiZGVsaXZlcnlDbGllbnRVcGRhdGVzIiwidHJ1RGVsaXZlcnlUZWFtTWVtYmVyc01vZGlmeSIsImxpYnJhcnlVc2VyIiwiVHJ1dGVzdGEtQ2VydGlmaWNhdGlvbi1BbGxvd0J5cGFzc0RhdGVWYWxpZGF0aW9uIiwiZGVsaXZlcnlTdGFuZGFyZHMiLCJzY2hlZHVsZUNvbW11bmljYXRpb25zIiwiY2VydGlmaWNhdGlvblVzZXIiLCJ0cnV0ZXN0YS10ZXN0cGxhbnMiLCJkZWxpdmVyeS1yZWFkLW9ubHkiLCJ0cnVEZWxpdmVyeVZpZXdSb2xlcyIsImVkaXRUZXN0aW5nTG9jYXRpb24iLCJ0cnV0ZXN0YS1kZWxpdmVyYWJsZXMtZXhwb3J0IiwidHJ1RGVsaXZlcnlBY3Rpdml0eURlbGV0ZVNoaWZ0IiwidHJ1dGVzdGEtdWxjIiwidHJ1dGVzdGEtb3JnYW5pemF0aW9uLWRlbGV0ZSIsInRydXRlc3RhLWRlbGl2ZXJhYmxlcy1jb250YWN0cyIsInRydXRlc3RhLXVzZXJzIiwidHJ1dGVzdGEtaW5zcGVjdGlvbnMiLCJ0cnVTY2hlZHVsaW5nQ2FuVHJhc2hTY2hlZHVsZSIsInRydXRlc3RhLWxpYnJhcnkiLCJjcmVhdGVDb21wb25lbnRTZWxlY3Rpb25zIiwidHJ1dGVzdGFfY3VzdG9tZXItZGVsZXRlIiwic2NoZWR1bGVEZWxpdmVyeSIsInRydXRlc3RhLWRlbGl2ZXJ5IiwidHJ1dGVzdGEtb3JnYW5pemF0aW9uLW1vZGlmeSIsInRydURlbGl2ZXJ5Q2FuQWRkQWN0aXZpdHlUaW1lIiwidHJ1dGVzdGEtZGVsaXZlcmFibGVzLWxvY2staW50ZWdyYXRpb25zIiwiaXNEZXZlbG9wZXIiLCJ0cnV0ZXN0YS1kZWxpdmVyYWJsZXMtd2l0aGRyYXciLCJzY2hlZHVsZVBvcnRhbCIsInNjaGVkdWxlTWFuYWdlIiwidHJ1dGVzdGEtYWNjcmVkaXRhdGlvbiIsInRydXRlc3RhLWRlbGl2ZXJhYmxlcy1yZXZpc2UiLCJkb2N1bWVudC5hZG1pbiIsInRydXRlc3RhLWN1c3RvbWVyLW1vZGlmeSIsInRydXRlc3RhLWN1c3RvbWVyLWRlbGV0ZSIsImNvbXBvbmVudHNVc2VyIiwidHJ1dGVzdGEtY29udGFjdC1hY3RpdmF0ZSIsInRydXRlc3RhLWRlbGl2ZXJhYmxlcy1leHBvcnQtYXVkaXQiLCJ0cnV0ZXN0YS1jcm0tY2hhbmdlLWN1c3RvbWVyLWluZm8iLCJ0cnV0ZXN0YS1kZWxpdmVyeS1hZG1pbiIsInRydXRlc3RhLXByb2plY3RzIiwiZGVsaXZlcmFibGVzLWludGVncmF0aW9ucyIsInRydXRlc3RhLWNvbnRhY3QtbW9kaWZ5Iiwic2NoZWR1bGVTdW1tYXJ5IiwidHJ1c2NoZWR1bGVDYW5Gb3JlY2FzdEFsbEFjdGl2aXRpZXMiLCJ0cnV0ZXN0YS1zY2hlZHVsaW5nIiwiZWRpdENvbXBvbmVudEZlZSIsInRydXRlc3RhLXByb2plY3RzLWFkbWluIiwiZGVsaXZlcnlTYW1wbGVUcmFja2VyIiwiZGVsaXZlcnlUZXN0UGxhbnMiLCJ0cnVEZWxpdmVyeUNhblNlbmRTY2hlZHVsZVVwZGF0ZSIsInRydXRlc3RhLWN1c3RvbWVyLWFkZCIsImNsaWVudC1kZWxpdmVyYWJsZXMtZG93bmxvYWQtZG9jdW1lbnRzIiwidHJ1dGVzdGEtZGVsaXZlcmFibGVzLWNvcHktcmV2aXNlZC1kb2N1bWVudHMiLCJlcXVpcG1lbnRVc2VyIiwiY2FuVmlld1NjaGVkdWxlVXBkYXRlc1RhYiIsInNjaGVkdWxpbmdVc2VyIiwiY29tcG9uZW50VGVzdGluZ0N1c3RvbWVyQWN0aW9ucyIsImVzdGltYXRlVXNlciIsInRydXRlc3RhUG9ydGFsQ2FuUmVnaXN0ZXIiLCJ1bWFfcHJvdGVjdGlvbiIsInJlcG9ydHMtcmVwb3NpdG9yeS1yZXZpc2UiLCJ0cnV0ZXN0YS1wcm9qZWN0LWFkbWluIiwic2NoZWR1bGVPcmRlciIsImRlbGl2ZXJ5UmV2aWV3cyIsInRydXRlc3RhLWNlcnRpZmljYXRpb24iLCJ0cnVTY2hlZHVsaW5nQ2FuQXNzaWduVGltZXNoZWV0IiwidHJ1dGVzdGEtY29udGFjdC1pbmFjdGl2YXRlIiwidHJ1dGVzdGEtZGVsaXZlcmFibGVzLXV0aWxpdGllcyIsInRydURlbGl2ZXJ5QWN0aXZpdHlTdGF0dXMiLCJ0cnVEZWxpdmVyeVRlYW1NZW1iZXJzQWRkIiwidHJ1dGVzdGEtdGVuYW50cyIsImRvd25sb2FkU2VsZWN0aW9uTm90aWNlcyIsImRlbGl2ZXJ5Q29tbWVudHMiLCJTZWFyY2hDb21wb25lbnRzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6IjJjMjA0ZjYwLWMyYTUtNDExMi05MzY0LTczZTBlNzc2OGNmNCIsInRlbmFudElkIjoiNzFhMjY3ZDItN2EwOC0xMWU3LWJiMzEtYmUyZTQ0YjA2YjM0IiwibmFtZSI6IlJvYnluIEhpbGxzIiwidGVuYW50VXNlcklkIjoiY2MzZDdmYjAtZjM4Ny00Y2I0LWJjMzgtYTYxZGM5NzM3ZmYxIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicm9ieW4uaGlsbHNAc2VtYXRyZWUuY29tIiwiZ2l2ZW5fbmFtZSI6IlJvYnluIiwiZmFtaWx5X25hbWUiOiJIaWxscyIsImVtYWlsIjoicm9ieW4uaGlsbHNAc2VtYXRyZWUuY29tIn0.t03F9k8bFF7aFDxRuP2s3qb9dTiMcdMo3WwPqEsofLItdOsN6ou0YO-dHqmt8Dz_B0bN9qPjCBrfhvGXQILid3U2Wh6_Ih9hPpWeztovVIGnIMborrRnzOxvG64NsA54WJnOfhpnAXioE4_a2gOyOvMY5Mq0l1TU64CCr6coVzh7qrdiaqpJTvgzWTxlWLGvZBAYZKLwVIRPd4HjRW0kZeMTwyiF3Ke0NT6fNS0b4R1dEtgl1ZF3iQ0ogDW3KlaOA7GjVJgkjjaXZw1hvwX46aOoaHbROet_CaIx323dw41pREmIP6QnRstcpT8AJ6EOybhIuH-cMqbOTYAxRQBKFA",
         #      "Content-Type": "application/json;charset=UTF-8"
         # }
         response = requests.get(new_url)
         header = response.headers
         print(type(header))
         print(header)
         status_code = response.status_code
         print(status_code)
         print(response.text)

         # print(response.json())
         # print(data)
         time.sleep(2)





