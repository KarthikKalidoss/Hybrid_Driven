import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec


class login:
    # *************************Login*************************

    input_box_username_id = "Input_Email"
    input_box_password_id = "Input_Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    button_logout_xpath = "//button[contains(text(),'Logout')]"
    button_confirm_logout = "//button[contains(text(),'Yes - Logout')]"

    # ********************SETUP-DRIVER***********************

    def __init__(self, driver):
        self.driver = driver

    # ****************SETUP-USERNAME AND PASSWORD************

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
