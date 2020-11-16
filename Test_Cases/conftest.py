from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture()
def driver_setup(browser):
    if browser == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
        driver.maximize_window
        print("..............LAUNCHING INTERNET EXPLORER BROWSER.........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
        print("..............LAUNCHING EDGE BROWSER.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        print("..............LAUNCHING FIREFOX BROWSER.........")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("..............LAUNCHING CHROME BROWSER.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# **************** pytest HTML Report *******************

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'CAF ADMIN'
    config._metadata['Module Name'] = 'LOGIN'
    config._metadata['Tester'] = 'KARTHIK KALIDOSS'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
