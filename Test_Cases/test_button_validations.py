import pytest
import allure
from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import login
from Utilities.CustomLogger import LogGen


class Test_003_button_validation:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_buttons_validation(self, driver_setup):
        self.logger.info('***********************Test_003_BUTTON-VALIDATIONS************************** ')
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

        # ************CHECK THE EXCEPTIONAL ENTRIES BUTTON IS ENABLED*********

        self.exceptional_entries = login(self.driver)
        exc_enabled = self.exceptional_entries.Exceptional_Button(self)
        if exc_enabled is not False:
            assert True
            print('EXCEPTIONAL ENTRIES BUTTON IS ENABLED - PASSED')
            self.logger.info('********* EXCEPTIONAL ENTRIES BUTTON VALIDATION IS PASSED ****************')
        else:
            print('EXCEPTIONAL ENTRIES BUTTON IS NOT-ENABLED - FAILED')
            self.logger.error('********* EXCEPTIONAL ENTRIES BUTTON VALIDATION IS FAILED ****************')
            assert False

        # ****************CHECK THE CLC INVOICE BUTTON IS ENABLED *********

        self.clc = login(self.driver)
        clc_enabled = self.clc.CLC_Button(self)
        if clc_enabled is not False:
            assert True
            print('CLC BUTTON IS ENABLED - PASSED')
            self.logger.info('********* CLC BUTTON VALIDATION IS PASSED ****************')
        else:
            print('CLC BUTTON IS NOT-ENABLED - FAILED')
            self.logger.error('********* CLC BUTTON VALIDATION IS FAILED ****************')
            assert False

        # ****************CHECK THE CERT DATE AND ENTRIES BUTTON IS ENABLED *********

        self.cert_date = login(self.driver)
        cert_date_enabled = self.cert_date.Certificate_Date_Button(self)
        if cert_date_enabled is not False:
            assert True
            print('CERTIFICATE DATE BUTTON IS ENABLED - PASSED')
            self.logger.info('********* CERTIFICATE DATE BUTTON VALIDATION TEST IS  PASSED ****************')
        else:
            print('CERTIFICATE DATE BUTTON IS NOT-ENABLED - FAILED')
            self.logger.error('********* CERTIFICATE DATE BUTTON VALIDATION TEST IS FAILED ****************')
            assert False

        # ****************CHECK THE CERTIFICATION RE-PRINT  BUTTON IS ENABLED *********

        self.cert_reprint = login(self.driver)
        cert_reprint_enabled = self.cert_reprint.Certificate_Reprint_Button(self)
        if cert_reprint_enabled is not False:
            assert True
            print('CERTIFICATE RE-PRINT BUTTON IS ENABLED - PASSED')
            self.logger.info('********* CERTIFICATE RE-PRINT BUTTON VALIDATION TEST IS PASSED ****************')
        else:
            print('CERTIFICATE RE-PRINT BUTTON IS NOT-ENABLED - FAILED')
            self.logger.error('********* CERTIFICATE RE-PRINT BUTTON VALIDATION TEST IS FAILED ****************')
            assert False

        # ****************CHECK THE AAR BUTTON IS ENABLED *********

        self.aar_button = login(self.driver)
        aar_button_enabled = self.aar_button.AAR_Button(self)
        if aar_button_enabled is not False:
            assert True
            print('ASSESSMENT ARRANGEMENTS VALID  VALUES BUTTON IS ENABLED - PASSED')
            self.logger.info('**** ASSESSMENT ARRANGEMENTS VALID  VALUES BUTTON VALIDATION TEST IS PASSED *****')
        else:
            print('ASSESSMENT ARRANGEMENTS VALID  VALUES BUTTON IS NOT ENABLED - FAILED')
            self.logger.error('***** ASSESSMENT ARRANGEMENTS VALID  VALUES BUTTON VALIDATION TEST IS FAILED *******')
            assert False

        # # ****************CHECK THE RELEASE VERIFICATION HOLD BUTTON IS ENABLED *********
        #
        # self.verification_hold = login(self.driver)
        # verification_hold_button = self.verification_hold.button_release_verification(self)
        # if verification_hold_button is not False:
        #     assert True
        #     print('RELEASE VERIFICATION ON HOLDS BUTTON IS ENABLED - PASSED')
        #     self.logger.info('**** RELEASE VERIFICATION ON HOLDS BUTTON VALIDATION TEST IS PASSED *****')
        # else:
        #     print('RELEASE VERIFICATION ON HOLDS BUTTON IS NOT ENABLED - FAILED')
        #     self.logger.info('***** RELEASE VERIFICATION ON HOLDS BUTTON VALIDATION TEST IS FAILED *******')
        #     assert False

        # *********** Login and button is enabled*********************

        self.user_button = login(self.driver)
        self.user_button.manage_Button()

        self.user_button_enabled = login(self.driver)
        user_button = self.user_button_enabled.enabled_button(self)
        if user_button is not True:
            assert True
            self.logger.info('********* USER NAME PROFILE BUTTON IS NOT ENABLED - PASSED ****************')
        else:
            self.driver.close()
            self.logger.info('********* USER NAME BUTTON IS ENABLED - FAILED ****************')
            assert False

        # ****************** LOG-OUT AND CLOSE THE BROWSER ***********************
        self.lo = login(self.driver)
        self.lo.click_logout()
        # self.lo.confirm_logout()
        self.driver.close()
        self.logger.info('*****************END OF BUTTON VALIDATION TEST*****************')
        self.logger.info('****************END OF Test_003_BUTTONS VALIDATIONS*****************')
