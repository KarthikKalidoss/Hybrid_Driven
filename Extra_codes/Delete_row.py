import time

from pywin.tools import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random
from faker import Faker

# *************************Driver-SetUp*************************
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://wtbizv01:57234/Identity/Account/Login?ReturnUrl=%2F')
driver.maximize_window()
print(driver.title)
wait = WebDriverWait(driver, 10)

# *************************Login*************************
Username = 'karthik.kalidoss@sqa.org.uk'
Password = 'Demodemo6781$'
username = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='Input_Email']")))
username.clear()
username.send_keys(Username)

password = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='Input_Password']")))
password.clear()
password.send_keys(Password)

# *****************************Login-Button********************************

Login = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Log in')]"))).click()

# **************************************************************************

support = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Support Live Admin')]"))).click()
aar = wait.until(
    ec.visibility_of_element_located((By.XPATH, "//body/div[1]/main[1]/div[2]/div[5]/div[1]/div[1]/a[1]"))).click()

dropdown = wait.until(ec.visibility_of_element_located((By.XPATH, "//select[@id='aaValidValueModel_categoryId']")))
dropdown.click()
# dropdown.deselect_by_value("Please select a Category")

drp = Select(dropdown)
drp.options[0].length = 0


# drp.options[0].remove()
print(len(drp.options))

all_options = drp.options
for option in all_options:
    print(option.text)

x = random.choice(all_options)
x.click()

time.sleep(5)
retrive = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Retrieve Valid Values')]")))
retrive.click()

category_id = driver.find_element_by_tag_name('h3').text
print(category_id)

#
time.sleep(5)
category_id1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//tbody/tr[1]/td[1]/input[1]"))).click()

time.sleep(5)
value1 = wait.until(
    ec.visibility_of_element_located((By.XPATH, "//input[@id='aaValidValueModels_0__value1']"))).get_attribute("value")

time.sleep(5)
value2 = wait.until(
    ec.visibility_of_element_located((By.XPATH, "//input[@id='aaValidValueModels_0__value2']"))).get_attribute("value")

print('THE SELECTED VALUES ARE => ', value1, ' AND ', value2)

select_delete = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@id='delete_btn']")))
select_delete.click()

alert = driver.switch_to.alert
message = alert.text
print('ALERT BOX SHOWS THE FOLLOWING MESSAGE => ' + message)

time.sleep(5)

alert.accept()

print('CLICKED OK ON THE ALERT WINDOW')

print('THE DELETED VALUES ARE ', value1, ' AND ', value2)

# //input[@id='aaValidValueModels_0__value1']/following::td[1]
