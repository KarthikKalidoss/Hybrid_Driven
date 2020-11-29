import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import login
from Utilities.CustomLogger import LogGen


class Test_004_login:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

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
            self.exc_entries = login(self.driver)
            self.exc_entries.click_exceptional_processing()
            message = self.exc_entries.file_upload(self)
            if message == 'File has been processed successfully.':
                print('EXCEPTIONAL ENTRIES FILE PROCESSED SUCCESSFULLY  - TEST IS PASSED')
                assert True
                self.logger.info('*** EXCEPTIONAL ENTRIES FILE PROCESSED SUCCESSFULLY  - TEST IS PASSED ***' + message)
            else:
                print('EXCEPTIONAL ENTRY FILE PROCESS IS FAILED - TEST IS FAILED')
                self.driver.save_screenshot(".\\Screenshots\\" + "file_process_status1.png")
                self.driver.close()
                self.logger.error('******* EXCEPTIONAL ENTRY FILE PROCESS IS FAILED - TEST IS FAILED ******' + message)
                assert False


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_Login.png")
            self.driver.close()
            self.logger.error('*************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS FAILED *******************')
            assert False

        self.lo = login(self.driver)
        self.lo.click_logout()
        self.lo.confirm_logout()
        self.driver.close()
        self.logger.info('*****************END OF EXCEPTIONAL ENTRIES TEST*****************')
        self.logger.info('***************END OF Test_004_EXCEPTIONAL_ENTRIES*****************')
