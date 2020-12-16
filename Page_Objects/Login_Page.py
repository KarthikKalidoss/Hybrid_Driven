import selenium
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class login:
    # *************************WEB-ELEMENTS FOR LOG-IN BUTTON*************************

    input_box_username_id = "Input_Email"
    input_box_password_id = "Input_Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"

    # *************************WEB-ELEMENTS FOR LOG-OUT BUTTON*************************
    button_logout_xpath = "//header/nav[1]/div[1]/div[1]/ul[1]/li[2]/form[1]"
    button_confirm_logout = "//button[contains(text(),'Yes - Logout')]"

    # *************************WEB-ELEMENTS FOR MAIN FUNCTIONALITY BUTTONS*************************

    button_manage = "//a[@id='manage']"  # ------ WEB ELEMENT FOR LOGIN USER NAME
    button_enabled = "//input[@id='Username']"  # ----- WEB ELEMENT FOR PROFILE USER NAME (MY SERVICES)

    button_exceptional_processing = "//a[contains(text(),'Go to exceptional processing')]"
    button_clc = "//a[contains(text(),'Go to Invoice exemptions')]"
    button_certificate_date = "//a[contains(text(),'Add certification dates')]"
    button_certificate_reprint = "//a[contains(text(),'Create replacement certificate')]"
    button_AAR = "//body/div[1]/main[1]/div[2]/div[5]/div[1]/div[1]/a[1]"
    button_release_verification = "//body/div[1]/main[1]/div[2]/div[6]/div[1]/div[1]/a[1]"

    # ************************* WEB-ELEMENTS FOR CHOOSE FILE AND SUBMIT BUTTON ************************************

    choose_file = "//body/div[1]/main[1]/form[1]/div[1]/input[1]"
    submit_button_xpath = "//button[contains(text(),'Submit')]"

    # *************************WEB-ELEMENT FOR ALERT MESSAGE AFTER SUBMIT THE CSV FILE ****************************

    alert_message = "/html[1]/body[1]/div[1]/main[1]"

    # ********************SETUP-DRIVER***********************

    def __init__(self, driver):
        self.driver = driver

    # ****************SETUP USERNAME AND PASSWORD************

    def set_username(self, username):
        self.driver.find_element_by_id(self.input_box_username_id).clear()
        self.driver.find_element_by_id(self.input_box_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.input_box_password_id).clear()
        self.driver.find_element_by_id(self.input_box_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def confirm_logout(self):
        self.driver.find_element_by_xpath(self.button_confirm_logout).click()

    # *****************************MAIN FUNCTIONALITY BUTTONS METHODS*****************************************

    def Exceptional_Button(self, exe_enabled):
        # self.driver.find_element_by_xpath(self.button_exceptional_processing)
        exc_enabled = self.driver.find_element_by_xpath(self.button_exceptional_processing)
        print('EXCEPTIONAL ENTRIES BUTTON IS ENABLED - ', exc_enabled.is_enabled())

    def CLC_Button(self, clc_button):
        clc_button = self.driver.find_element_by_xpath(self.button_clc)
        print('CLC BUTTON IS ENABLED - ', clc_button.is_enabled())

    def Certificate_Date_Button(self, cert_date_button):
        cert_date_button = self.driver.find_element_by_xpath(self.button_certificate_date)
        print('CERTIFICATE DATE BUTTON IS ENABLED - ', cert_date_button.is_enabled())

    def Certificate_Reprint_Button(self, cert_reprint):
        cert_reprint = self.driver.find_element_by_xpath(self.button_certificate_reprint)
        print('CERTIFICATE RE-PRINT BUTTON IS ENABLED - ', cert_reprint.is_enabled())

    def AAR_Button(self, aar_button):
        aar_button = self.driver.find_element_by_xpath(self.button_AAR)
        print('ASSESSMENT ARRANGEMENTS VALID VALUES BUTTON IS ENABLED - ', aar_button.is_enabled())

    def Release_Verification_Button(self, release_verification):
        release_verification = self.driver.find_element_by_xpath(self.button_release_verification)
        print('RELEASE VERIFICATION ON HOLDS BUTTON IS ENABLED - ', release_verification.is_enabled())

    # ****************** LOGIN USER NAME BUTTON AND USER PROFILE BUTTON ENABLED METHOD *************************
    def manage_Button(self):
        self.driver.find_element_by_xpath(self.button_manage).click()

    def enabled_button(self, username_button):
        username_button = self.driver.find_element_by_xpath(self.button_enabled)
        print('USER NAME BUTTON IS ENABLED - ', username_button.is_enabled())

    # *************************** FUNCTIONALITY BUTTON CLICK FOR EXCEPTIONAL ENTRIES ***********************************
    def click_exceptional_processing(self):
        self.driver.find_element_by_xpath(self.button_exceptional_processing).click()

    # ********************************* CHOOSE FILE BUTTON FOR EXCEPTIONAL ENTRIES ************************************
    def file_upload(self, selected_file):
        selected_file = self.driver.find_element_by_xpath(self.choose_file)

        # ********************************* SELECT ONE CSV FILES ****************************************************
        selected_file.send_keys("C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Exceptional_Entries.csv")

        # ********************************* SELECT TWO CSV FILES ****************************************************
        # selected_file.send_keys("C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Exceptional_Entries.csv \n "
        #                         "C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Exceptional_Entries1.csv ")

        self.driver.find_element_by_xpath(self.submit_button_xpath).submit()
        message = self.driver.find_element_by_xpath(self.alert_message).text
        return message

    # ****************************END OF FUNCTIONALITY BUTTON CLICK FOR EXCEPTIONAL ENTRIES **************************

    # *************************** FUNCTIONALITY BUTTON CLICK FOR CLC INVOICE *****************************************
    def click_clc_exemptions(self):
        self.driver.find_element_by_xpath(self.button_clc).click()

    # *********************************** CHOOSE FILE BUTTON FOR CLC INVOICE****************************************
    def clc_file_upload(self, selected_file):
        selected_file = self.driver.find_element_by_xpath(self.choose_file)

        # ********************************* SELECT ONE CSV FILES ****************************************************
        selected_file.send_keys("C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/CLC_Exemptions.csv")

        # ********************************* SELECT TWO CSV FILES ****************************************************
        # selected_file.send_keys("C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Exceptional_Entries.csv \n "
        #                         "C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/Exceptional_Entries1.csv ")

        self.driver.find_element_by_xpath(self.submit_button_xpath).submit()
        message = self.driver.find_element_by_xpath(self.alert_message).text
        return message

    # ********************************** END OF CHOOSE FILE BUTTON FOR CLC INVOICE *********************************

    # **************** FUNCTIONALITY BUTTON CLICK FOR CERTIFICATE DATE AND ENTRY STATUS UPDATE**********************
    def click_certificate_date(self):
        self.driver.find_element_by_xpath(self.button_certificate_date).click()

    # *********************************** CHOOSE FILE BUTTON FOR CLC INVOICE****************************************
    def cert_date_file_upload(self, selected_file):
        selected_file = self.driver.find_element_by_xpath(self.choose_file)
        # ********************************* SELECT ONE CSV FILES ****************************************************
        selected_file.send_keys("C:/Karthik/New_Projects/Hybrid_Driven/Test_Data/CDES-Update.csv")
        self.driver.find_element_by_xpath(self.submit_button_xpath).submit()
        message = self.driver.find_element_by_xpath(self.alert_message).text
        return message

    # **************** END OF FUNCTIONALITY BUTTON CLICK FOR CERTIFICATE DATE AND ENTRY STATUS UPDATE******************
