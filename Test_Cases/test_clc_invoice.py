import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import login
from Utilities.CustomLogger import LogGen


class Test_005_clc_invoice:
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
            self.clc_exemptions = login(self.driver)
            self.clc_exemptions.click_clc_exemptions()
            message = self.clc_exemptions.clc_file_upload(self)
            if message == 'File has been processed successfully.':
                print('CLC INVOICE EXEMPTIONS FILE PROCESSED SUCCESSFULLY  - TEST IS PASSED')
                assert True
                self.logger.info('** CLC INVOICE EXEMPTIONS FILE PROCESSED SUCCESSFULLY - TEST IS PASSED **' + message)
            else:
                print('CLC INVOICE EXEMPTIONS FILE PROCESS IS FAILED - TEST IS FAILED')
                self.driver.save_screenshot(".\\Screenshots\\" + "clc_file_process_status.png")
                self.driver.close()
                self.logger.error('**** CLC INVOICE EXEMPTIONS FILE PROCESS IS FAILED - TEST IS FAILED ****' + message)
                assert False

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clc_exemptions.png")
            self.driver.close()
            self.logger.error('*************** CAF ADMIN PORTAL VALIDATION LOGIN TEST IS FAILED *******************')
            assert False

        self.lo = login(self.driver)
        self.lo.click_logout()
        # self.lo.confirm_logout()
        self.driver.close()
        self.logger.info('************* END OF CLC INVOICE EXEMPTIONS TEST *****************')
        self.logger.info('**************** END OF Test_004_CLC_INVOICE *****************')
