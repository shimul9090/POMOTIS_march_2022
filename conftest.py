import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Configuration.config import TestData

driver = None
@pytest.fixture(scope ='class')
def init_driver(request):
    td = TestData()
    ser = Service(td.DRIVER_EXEC)
    web_driver = webdriver.Chrome(service=ser)
    request.cls.driver = web_driver
    web_driver.get(td.URL)
    web_driver.maximize_window()
    web_driver.implicitly_wait(30)

    yield
    #web_driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass