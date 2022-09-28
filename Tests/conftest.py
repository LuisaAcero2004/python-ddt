import pytest
from selenium import webdriver

import Config.config


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=Config.config.TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path=Config.config.TestData.EDGE_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
