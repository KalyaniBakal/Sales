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
# for i in range(2):
#     sort_button = driver.find_element(By.ID, "sort_booking_details")
#     sort_button.click()
#     time.sleep(3)
# print("Sort button clicked.")
#
# start_date = datetime.date(2024, 11, 1)
# end_date = datetime.date(2024, 12, 31)
# random_start_date = generate_random_date(start_date, end_date)
# random_end_date = generate_random_date(random_start_date, end_date)
# formatted_random_start_date = random_start_date.strftime("%d-%m-%Y")
# formatted_random_end_date = random_end_date.strftime("%d-%m-%Y")
# start_date_input = driver.find_element(By.ID, "startDate")
# end_date_input = driver.find_element(By.ID, "endDate")
# start_date_input.send_keys(formatted_random_start_date)
# end_date_input.send_keys(formatted_random_end_date)
# end_date_input.send_keys(Keys.ESCAPE)
# print("Start date: " + formatted_random_start_date)
# print("End date: " + formatted_random_end_date)
#
# connection = databseConnection.conn()
# cursor = connection.cursor()
# query = "select booking_for from bookings;"
# cursor.execute(query)
# result = cursor.fetchall()
# customer_name = result[0][0]
# print(customer_name)
# search_input = driver.find_element(By.NAME, "bookingFor")
# search_input.send_keys(customer_name)
# time.sleep(5)
# dropdown_option_xpath = f"//div[@id='myDropdown_bookingFor']//span[contains(text(), '{customer_name}')]"
# dropdown_option = driver.find_element(By.XPATH, dropdown_option_xpath)
# dropdown_option.click()
# time.sleep(2)
#
#
# dropdown = driver.find_element(By.ID, "bookingType")
# select = Select(dropdown)
# options = select.options
# valid_options = options[1:]
# random_option = random.choice(valid_options)
# select.select_by_visible_text(random_option.text)
# print(f"Randomly selected option: {random_option.text}")
# time.sleep(2)
#
# dropdown = driver.find_element(By.ID, "bookingStatus")
# select = Select(dropdown)
# options = select.options
# valid_options = options[1:]
# random_option = random.choice(valid_options)
# select.select_by_visible_text(random_option.text)
# print(f"Randomly selected option: {random_option.text}")
# time.sleep(2)
#
# search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
# search_button.click()
# time.sleep(3)
# reset_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Reset all')]")
# reset_button.click()
# time.sleep(3)
#
# print("search successfully")
# time.sleep(3)
#
# driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[2]/a").click()
# time.sleep(3)
#
# driver.find_element(By.ID, 'EditBooking').click()
# time.sleep(2)
#
# wish_values = ["BP", "Headache", "Fever", "Cold", "Back Pain", "Migraine"]
# random_wish = random.choice(wish_values)
# wish_input = driver.find_element(By.ID, "wish")
# wish_input.send_keys(random_wish)
# print(f"Random wish entered: {random_wish}")
# time.sleep(4)
#
# timeInMins=driver.find_element(By.ID,"requestedTimeInMins")
# timeInMins.clear()
# timeInMins.send_keys("60")
#
# address_field = driver.find_element(By.ID, "address")
# full_address = generate_full_address()
# address_field.clear()
# address_field.send_keys(full_address)
# print("Updated Full Address:", full_address)
#
# start_date = datetime.date(2024, 11, 1)  # Example start date
# end_date = datetime.date(2024, 12, 31)  # Example end date
# random_start_date = generate_random_date(start_date, end_date)
# random_end_date = generate_random_date(random_start_date, end_date)
# formatted_random_start_date = random_start_date.strftime("%d-%m-%Y")
# formatted_random_end_date = random_end_date.strftime("%d-%m-%Y")
# start_date_input = driver.find_element(By.ID, "scheduledStartDate")
# end_date_input = driver.find_element(By.ID, "scheduledEndDate")
# start_date_input.clear()
# end_date_input.clear()
# start_date_input.send_keys(formatted_random_start_date)
# end_date_input.send_keys(formatted_random_end_date)
# end_date_input.send_keys(Keys.ESCAPE)
# print("Start date: " + formatted_random_start_date)
# print("End date: " + formatted_random_end_date)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
# driver.find_element(By.ID,"submit").click()
# time.sleep(2)
#
# wait = WebDriverWait(driver, 10)
# ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]")))
#
# # Click the button
# ok_button.click()
# print("Button with 'OK' text clicked successfully!")
#
# print("Update successfully")
# driver.execute_script("window.scrollTo(0, 0);")
# time.sleep(3)

driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[2]/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='View Payment']").click()
time.sleep(3)  # Wait for the modal to appear

# Use JavaScript to click the close button
driver.execute_script("document.querySelector('button.btn.text-white[data-bs-dismiss=\"modal\"]').click()")
time.sleep(5)



try:
    driver.find_element(By.XPATH, "//button[text()='View EMI details']").click()
    time.sleep(2)
    elements = driver.find_elements(By.CSS_SELECTOR, "i.bi.bi-image.text-primary.fs-5.ms-3")
    if elements:
        print("Element found:", elements[0].get_attribute("class"))
        elements[0].click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        close_button = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-x-lg")
        print("Element found:", close_button.get_attribute("class"))
        close_button.click()
    else:
        print("Element not found. Performing alternative action.")

finally:
    driver.find_element(By.XPATH, "//button[text()='Upload Customer Photo']").click()
    time.sleep(4)

file_input = driver.find_element(By.ID, "input-file")
driver.execute_script("arguments[0].value = '';", file_input)

file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/boy.jpeg")
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='UPLOAD PHOTO']").click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
try:
    ok_button = wait.until(EC.element_to_be_clickable((By.ID, "global_Success_Message_Btn")))
    ok_button.click()
    time.sleep(3)
except:
    ok_button = wait.until(EC.element_to_be_clickable((By.ID, "global_Error_Message_Btn")))
    ok_button.click()
    time.sleep(3)


driver.find_element(By.XPATH, "//button[text()='View Customer Photos']").click()
time.sleep(4)
try:
    images = driver.find_elements(By.XPATH, "//div[@class='col-sm-12']//img")
    random_image = random.choice(images)
    driver.execute_script("arguments[0].scrollIntoView();", random_image)
    ActionChains(driver).move_to_element(random_image).click().perform()
    print(f"Clicked on image with src: {random_image.get_attribute('src')}")
finally:
    driver.execute_script("document.querySelector('i.bi.bi-x-lg').click()")
time.sleep(5)

time.sleep(3)
driver.quit()