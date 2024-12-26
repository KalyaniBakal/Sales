import random
import string
import time
from datetime import timedelta

from loguru._datetime import datetime
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select

import databseConnection
from Functions import generate_random_name, generate_random_email, generate_random_description, \
    generate_unique_phone_number, generate_random_4_digit_time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://185.199.53.169:5000/login")

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

def freeBooking(driver):
    driver.get("http://185.199.53.169:5000/bookings")

    driver.find_element(By.XPATH, "//button[contains(text(), '+ Create New')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Free Booking')]").click()

    print("Clicked the Free Booking button successfully.")
    time.sleep(2)

    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "select name from marketing_leads ;"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "Lead_name-1")
    search_input.send_keys(customer_name)
    time.sleep(5)
    dropdown_option_xpath = f"//div[@id='myDropdown-lead-1']//span[contains(text(), '{customer_name}')]"
    dropdown_option = driver.find_element(By.XPATH, dropdown_option_xpath)
    dropdown_option.click()
    time.sleep(2)

    addresses = [
        "123 Main Street, Springfield",
        "456 Elm Street, Metropolis",
        "789 Maple Avenue, Gotham",
        "321 Oak Lane, Smallville",
        "654 Pine Road, Star City",
        "987 Birch Boulevard, Central City"
    ]
    random_address = random.choice(addresses)
    address_input = driver.find_element(By.ID, "address_free")
    address_input.clear()
    address_input.send_keys(random_address)
    time.sleep(4)

    wish_values = ["BP", "Headache", "Fever", "Cold", "Back Pain", "Migraine"]
    random_wish = random.choice(wish_values)
    wish_input = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[2]/form/div[4]/div[1]/input")
    wish_input.send_keys(random_wish)
    print(f"Random wish entered: {random_wish}")
    time.sleep(4)

    query = "SELECT first_name FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "ReferredBy-1")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH, f"//div[@id='myDropdown-1']//span[contains(text(), '{customer_name}')]").click()
    time.sleep(2)

    Starttime_input = driver.find_element(By.ID, "Start_timeInput-1")
    random_start_time = generate_random_4_digit_time()
    Starttime_input.send_keys(random_start_time)
    time.sleep(4)
    driver.execute_script("document.getElementById('start_time_pm-1').checked = true;")

    Endtime_input = driver.find_element(By.ID, "End_timeInput-1")
    random_end_time = generate_random_4_digit_time()
    Endtime_input.send_keys(random_end_time)
    driver.execute_script("document.getElementById('end_time_pm-1').checked = true;")
    time.sleep(2)

    textarea = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[2]/form/div[7]/div/textarea")
    random_instruction = generate_random_description()
    textarea.send_keys(random_instruction)

    time.sleep(3)
    create_booking_button = driver.find_element(By.CSS_SELECTOR,
                                                "#FREE_booking > div > div > div.modal-footer.d-flex.justify-content-center.border.border-1 > div > div > button.btn.btn-primary.btn-sm")

    create_booking_button.click()

    # Wait and close browser
    time.sleep(5)

    time.sleep(2)
    print("Free booking created")
    try:
        driver.find_element(By.ID, "global_Error_Message_Model").click()
        print("Click on error msg")
    except:
        driver.find_element(By.ID, "global_Success_Message_Model").click()
        print("Click on success msg")
    time.sleep(2)


