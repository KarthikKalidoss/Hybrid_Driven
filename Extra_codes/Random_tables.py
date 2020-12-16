import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random
from faker import Faker

faker = Faker()

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
drp = Select(dropdown)

# select random dropdown
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

num_rows = len(driver.find_elements(By.XPATH, "//tbody/tr"))
print('TOTAL NUMBER OF ROWS IN ' + category_id + ' is = ', num_rows)

num_column = len(wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//tbody/tr[1]/td"))))
print('TOTAL NUMBER OF COLUMNS IN  = ' + category_id + ' is = ', num_column)


before_XPath_1 = "//*[@id='customers']/tbody/tr[1]/th["
before_XPath_2 = "//*[@id='customers']/tbody/tr[2]/td["
after_XPath = "]"

# for t_col in range(1, (num_column + 1)):
#     FinalXPath = before_XPath_1 + str(t_col) + after_XPath
#     cell_text = driver.find_element_by_xpath(FinalXPath).text
#     print(cell_text)


driver.close()
driver.quit()
