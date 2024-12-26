import datetime
import logging
import random
import string
import time
from datetime import timedelta

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select

import databseConnection
from Functions import random_name, generate_random_description, generate_random_date, generate_random_4_digit_time, \
    generate_random_name, generate_unique_phone_number, generate_full_address

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://185.199.53.169:5000/login")
time.sleep(2)
username_field = driver.find_element(By.NAME, "username")  # Replace with actual name attribute
password_field = driver.find_element(By.NAME, "password")  # Replace with actual name attribute

username_field.send_keys("9359146811")  # Replace with correct username or phone number
password_field.send_keys("Kalyani@1234")
password_field.send_keys(Keys.RETURN)

print(driver.current_url)
if "/dashboard" in driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")

driver.get("http://185.199.53.169:5000/bookings")

#--------------------FILTER--------------------------------------------

start_date = datetime.date(2024, 11, 1)  # Example start date
end_date = datetime.date(2024, 12, 31)  # Example end date
random_start_date = generate_random_date(start_date, end_date)
random_end_date = generate_random_date(random_start_date, end_date)
formatted_random_start_date = random_start_date.strftime("%d-%m-%Y")
formatted_random_end_date = random_end_date.strftime("%d-%m-%Y")
start_date_input = driver.find_element(By.ID, "startDate")
end_date_input = driver.find_element(By.ID, "endDate")
start_date_input.send_keys(formatted_random_start_date)
end_date_input.send_keys(formatted_random_end_date)
end_date_input.send_keys(Keys.ESCAPE)
print("Start date: " + formatted_random_start_date)
print("End date: " + formatted_random_end_date)

connection = databseConnection.conn()
cursor = connection.cursor()
query = "select booking_for from bookings;"
cursor.execute(query)
result = cursor.fetchall()
customer_name = result[0][0]
print(customer_name)
search_input = driver.find_element(By.NAME, "bookingFor")
search_input.send_keys(customer_name)
time.sleep(5)
dropdown_option_xpath = f"//div[@id='myDropdown_bookingFor']//span[contains(text(), '{customer_name}')]"
dropdown_option = driver.find_element(By.XPATH, dropdown_option_xpath)
dropdown_option.click()
time.sleep(2)


dropdown = driver.find_element(By.ID, "bookingType")
select = Select(dropdown)
options = select.options
valid_options = options[1:]
random_option = random.choice(valid_options)
select.select_by_visible_text(random_option.text)
print(f"Randomly selected option: {random_option.text}")
time.sleep(2)

dropdown = driver.find_element(By.ID, "bookingStatus")
select = Select(dropdown)
options = select.options
valid_options = options[1:]
random_option = random.choice(valid_options)
select.select_by_visible_text(random_option.text)
print(f"Randomly selected option: {random_option.text}")
time.sleep(2)

search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
ActionChains(driver).move_to_element(search_button).perform()
time.sleep(3)
search_button = driver.find_element(By.XPATH, "//button[text()='Reset all']")
ActionChains(driver).move_to_element(search_button).perform()
time.sleep(3)

print("search successfully")
time.sleep(3)

driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[2]/a").click()
time.sleep(3)

driver.find_element(By.ID, 'EditBooking').click()
time.sleep(2)

wish_values = ["BP", "Headache", "Fever", "Cold", "Back Pain", "Migraine"]
random_wish = random.choice(wish_values)
wish_input = driver.find_element(By.ID, "wish")
wish_input.send_keys(random_wish)
print(f"Random wish entered: {random_wish}")
time.sleep(4)

timeInMins=driver.find_element(By.ID,"requestedTimeInMins")
timeInMins.clear()
timeInMins.send_keys("60")

address_field = driver.find_element(By.ID, "address")
full_address = generate_full_address()
address_field.clear()
address_field.send_keys(full_address)
print("Updated Full Address:", full_address)

start_date = datetime.date(2024, 11, 1)  # Example start date
end_date = datetime.date(2024, 12, 31)  # Example end date
random_start_date = generate_random_date(start_date, end_date)
random_end_date = generate_random_date(random_start_date, end_date)
formatted_random_start_date = random_start_date.strftime("%d-%m-%Y")
formatted_random_end_date = random_end_date.strftime("%d-%m-%Y")
start_date_input = driver.find_element(By.ID, "scheduledStartDate")
end_date_input = driver.find_element(By.ID, "scheduledEndDate")
start_date_input.clear()
end_date_input.clear()
start_date_input.send_keys(formatted_random_start_date)
end_date_input.send_keys(formatted_random_end_date)
end_date_input.send_keys(Keys.ESCAPE)
print("Start date: " + formatted_random_start_date)
print("End date: " + formatted_random_end_date)



driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[1]/div[3]/div/button").click()
driver.execute_script("document.querySelector('i.bi.bi-x-lg').click()")
time.sleep(5)

driver.execute_script("document.querySelector('div:nth-child(4) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > form > div:nth-child(6) > div:nth-child(2) > button').click()")


time.sleep(3)
driver.quit()