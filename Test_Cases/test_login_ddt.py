import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import login
from Utilities.CustomLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_login:
    url = ReadConfig.getApplicationURL()
    path = './/Test_Data/Login_Data.xlsx'

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, driver_setup):
        self.logger.info('***********************Test_002_DDT_Login************************** ')
        self.logger.info('VERIFYING CAF ADMIN LOGIN VALIDATION - DATA DRIVEN TEST')
        self.driver = driver_setup
        self.driver.get(self.url)
        self.lp = login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('NUMBER OF ROWS IN THE EXCEL : ', self.rows)

        lst_status = []  # EMPTY LIST VARIABLE

        # ********** READ DATA FROM EXCEL FILE*****************************
        for r in range(2, self.rows + 1):
            self.User_Name = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.Password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.Expected = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.set_username(self.User_Name)
            self.lp.set_password(self.Password)
            self.lp.click_login()

            actual_title = self.driver.title
            Expected_tile = 'Home Page - SQA.Net.LiveAdmin'

            if actual_title == Expected_tile:
                if self.Expected == 'PASS':
                    self.logger.info('*************** CAF ADMIN LOGIN VALIDATION TEST IS PASSED *******************')
                    self.lo = login(self.driver)
                    self.lo.click_logout()
                    self.lo.confirm_logout()

                    lst_status.append('PASSED')
                elif self.Expected == 'FAIL':
                    self.logger.info('*************** CAF ADMIN LOGIN VALIDATION TEST IS FAILED *******************')

                    self.driver.close()
                    lst_status.append('FAILED')

            elif actual_title != Expected_tile:
                if self.Expected == 'PASS':
                    self.logger.info('*************** CAF ADMIN LOGIN VALIDATION TEST IS FAILED *******************')

                    lst_status.append('FAILED')
                elif self.Expected == 'FAIL':
                    self.logger.info('*************** CAF ADMIN LOGIN VALIDATION TEST IS PASSED *******************')
                    lst_status.append('PASSED')
            print(lst_status)

        if 'FAILED' not in lst_status:
            self.logger.info('CAF ADMIN LOGIN VALIDATION - DATA DRIVEN TEST IS PASSED')
            self.driver.close()
            assert True
        else:
            self.logger.info('CAF ADMIN LOGIN VALIDATION - DATA DRIVEN TEST IS FAILED')
            self.driver.close()
            assert False

        self.logger.info('*****************END OF DATA DRIVEN TEST*****************')
        self.logger.info('****************END OF Test_002_DDT_Login*****************')
