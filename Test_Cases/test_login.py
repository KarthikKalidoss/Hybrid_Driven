import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import login
from Utilities.CustomLogger import LogGen


class Test_001_login:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    # wait = WebDriverWait(driver, 10)

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Home_Page_Title(self, driver_setup):
        self.logger.info('*************** TEST_001_LOGIN *******************')
        self.logger.info('*************** VERIFYING URL / HOME PAGE TITLE *******************')
        self.driver = driver_setup
        self.driver.get(self.url)
        actual_title = self.driver.title
        if actual_title == "Log in | SQA Internal Portal":
            assert True
            self.driver.close()
            self.logger.info('*************** URL WORKING FINE AND HOME PAGE TITLE IS PASSED *******************')

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + " Test_Home_Page_Title.png")
            self.driver.close()
            self.logger.error('*************** URL AND HOME PAGE TITLE IS FAILED *******************')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, driver_setup):
        self.logger.info('*************** VERIFYING CAF ADMIN PORTAL VALIDATION *******************')
        self.driver = driver_setup
        self.driver.get(self.url)
        self.lp = login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title = self.driver.title
        if actual_title == 'Home Page - SQA.Net.LiveAdmin':
            assert True
            self.logger.info('*************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS PASSED *******************')

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_Login.png")
            self.driver.close()
            self.logger.error('*************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS FAILED *******************')
            assert False

        self.lo = login(self.driver)
        self.lo.click_logout()
        self.lo.confirm_logout()
        self.driver.close()
