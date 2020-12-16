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

# *************************Driver-SetUp*******************************************
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://wtbizv01:57234/Identity/Account/Login?ReturnUrl=%2F')
driver.maximize_window()
print(driver.title)
wait = WebDriverWait(driver, 10)

# *************************Login***************************************************
Username = 'karthik.kalidoss@sqa.org.uk'
Password = 'Demodemo6781$'
username = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='Input_Email']")))
username.clear()
username.send_keys(Username)

password = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='Input_Password']")))
password.clear()
password.send_keys(Password)

# *****************************Login-Button****************************************

Login = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Log in')]"))).click()

# ********************************************************************************

support = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Support Live Admin')]"))).click()
aar = wait.until(
    ec.visibility_of_element_located((By.XPATH, "//body/div[1]/main[1]/div[2]/div[5]/div[1]/div[1]/a[1]"))).click()

dropdown = wait.until(ec.visibility_of_element_located((By.XPATH, "//select[@id='aaValidValueModel_categoryId']")))
drp = Select(dropdown)

# drp.select_by_value('15')
# drp.select_by_visible_text('7 - PA Referral')

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

num_rows = len(driver.find_elements(By.XPATH, "//tbody/tr"))
print('TOTAL NUMBER OF ROWS IN ' + category_id + ' is = ', num_rows)

num_column = len(wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//tbody/tr[1]/td"))))
print('TOTAL NUMBER OF COLUMNS IN  = ' + category_id + ' is = ', num_column)

time.sleep(5)
insert = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Insert New')]")))
insert.click()

time.sleep(5)
value1 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#aaValidValueModels_0__newValue1")))
a = random.randint(10, 50)
value1.send_keys(a)
print('THE INPUT FOR VALUE - 1 IS ', a)

time.sleep(5)
value2 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#aaValidValueModels_0__newValue2")))
b = random.randint(51, 100)
value2.send_keys(b)
print('THE INPUT FOR VALUE - 2 IS ', b)

time.sleep(5)
insert_new = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Insert New')]")))
insert_new.click()

num_rows_after = len(driver.find_elements(By.XPATH, "//tbody/tr"))
print('TOTAL NUMBER OF ROWS IN ' + category_id + ', AFTER INSERT NEW VALUE IS => ', num_rows_after)

num_column_after = len(wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//tbody/tr[1]/td"))))
print('TOTAL NUMBER OF COLUMNS IN  = ' + category_id + ' AFTER INSERT NEW VALUE IS => ', num_column_after)

# Verify the presence of the given data
data1 = str(a)
data2 = str(b)
dataSize1 = len(driver.find_elements_by_xpath("//tbody/tr" + data1))
dataSize2 = len(driver.find_elements_by_xpath("//tbody/tr" + data2))
if dataSize1 & dataSize2 > 0:
    print(data1+ ' AND ' + data2 + 'THE DATA IS NOT PRESENCE')
else:
    print('BOTH THE VALUES '+ data1 + ' AND ' + data2 + ' IS PRESENT IN THE TABLE')
    print('TEST IS PASSED')

# rows = (driver.find_elements_by_xpath("//tbody/tr"))
# row = next(filter(lambda x: x.find_element_by_xpath("//tbody/tr[1]/td").text == a, rows))
# value = row.find_element_by_xpath('//tbody/tr').text

# faker = Faker()
#
# print(f'Name: {faker.name()}')
# print(f'First name: {faker.first_name()}')
# print(f'Last name: {faker.last_name()}')
# print(random.randint(10, 50))
#
# print('--------------------------')
#
# print(f'Male name: {faker.name_male()}')
# print(f'Female name: {faker.name_female()}')

# before_XPath_1 = "//tbody/tr["
# before_XPath_2 = "//tbody/tr[1]/td["
# after_XPath = "]"
#
