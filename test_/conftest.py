import pytest
from selenium import webdriver
import time
from Library.config import Config
from selenium.webdriver.firefox.options import Options

@pytest.fixture(params=["Edge","Chrome","Firefox"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_Driver_Path)

    elif request.param == "Firefox":
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path, options=options)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)


    driver.get(Config.Url)
    driver.maximize_window()
    time.sleep(2)
    driver.implicitly_wait(30)
    yield driver
    driver.save_screenshot("test_hoteloffers.png")
    time.sleep(2)
    driver.close()

