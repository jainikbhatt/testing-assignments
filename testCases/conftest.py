import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    driver = webdriver.Chrome('drivers/chromedriver.exe')
    driver.maximize_window()
    return driver
    # if browser == 'chrome':
    #     driver = webdriver.Chrome('drivers/chromedriver.exe')
    #     driver.maximize_window()
    #     print("Launching Chrome browser...............")
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox('drivers/geckodriver.exe')
    #     driver.maximize_window()
    #     print("Launching Firefox browser...............")
    # elif browser == 'edge':
    #     driver = webdriver.Edge('drivers/msedgedriver.exe')
    #     driver.maximize_window()
    #     print("launching Edge browser..................")
    # else:
    #     option = webdriver.ChromeOptions()
    #     option.headless = True
    #     driver = webdriver.Chrome('drivers/chromedriver.exe')
    #     driver.maximize_window()
    # return driver

#
# def pytest_addoption(parser):  # This will get the value from CLI / hooks
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

#
# ##################### Pytest HTML Report##################
#
# # It is hook for adding environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'UAT Kaptaine Dashboard'
#     config._metadata['Module Name'] = 'Dashboard User'
#     config._metadata['Tester'] = 'Jainik Bhatt'