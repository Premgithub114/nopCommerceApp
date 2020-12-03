# This is for cross browser testing. But its not working. Need to check later
'''
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:/Users/Prem/PycharmProjects/page_object_model_1/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox("C:/Users/Prem/Downloads/Drivers/geckodriver-v0.28.0-win64/geckodriver.exe")
    else:
        driver = webdriver.ie("C:/Users/Prem/Downloads/Drivers/IEDriverServer_Win32_3.141.0/IEDriverServer.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")    # This will take the input from the CLI

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")    # This will send the input to setup method above
'''
