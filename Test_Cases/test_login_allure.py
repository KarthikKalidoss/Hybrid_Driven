import allure
import pytest
from allure_commons.types import AttachmentType
from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import login
from Utilities.CustomLogger import LogGen


class Test_001_login:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    allure.severity_level(allure.severity_level.BLOCKER)

    def test_Home_Page_Title(self, driver_setup):
        self.logger.info('*************** TEST_001_LOGIN *******************')
        self.logger.info('*************** VERIFYING URL / HOME PAGE TITLE *******************')
        self.driver = driver_setup
        self.driver.get(self.url)
        actual_title = self.driver.title
        if actual_title == "Log in | SQA Internal Portal1":
            assert True
            self.driver.close()
            self.logger.info('*************** URL WORKING FINE AND HOME PAGE TITLE IS PASSED *******************')

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='Test_URL', attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + " Test_Home_Page_Title.png")
            self.driver.close()
            self.logger.error('*************** URL AND HOME PAGE TITLE IS FAILED *******************')
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_skip(self):
        pytest.skip("SKIPPING THE TEST, DO IT LATER.......")

    @allure.severity(allure.severity_level.CRITICAL)
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
        self.logger.info('*****************END OF URL AND LOGIN VALIDATION TEST*****************')
        self.logger.info('*******************END OF Test_001_login*****************')
