import subprocess
import uuid

import mysql.connector
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import random
import string
import time

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


driver.get("http://185.199.53.169:5000/offerings")
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "i.bi.bi-sort-up").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, "i.bi.bi-plus-lg").click()
# time.sleep(2)


def generate_unique_offering_id():
    connection = mysql.connector.connect(
        host="185.199.53.169",
        user="lovenheal_user",
        password="lovenheal_user",
        database="lovenheal_server"
    )
    cursor = connection.cursor()

    while True:

        offering_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return offering_id

        query = "SELECT COUNT(*) FROM offerings WHERE offering_id = %s"
        cursor.execute(query, (offering_id,))
        result = cursor.fetchone()

        # If no records found with the generated ID, it’s unique
        if result[0] == 0:
            break

    # Close the connection
    cursor.close()
    connection.close()

    return offering_id

time.sleep(2)
unique_offering_id = generate_unique_offering_id()
offering_id_field = driver.find_element("id", "offeringId")
offering_id_field.send_keys(unique_offering_id)

driver.find_element("id", "offeringName").send_keys("Sample Offering Name")

offering_type_dropdown = Select(driver.find_element("id", "offeringType"))
offering_type_dropdown.select_by_visible_text("Service")

filename_input = driver.find_element("id", "fileName")
filename_input.send_keys("example_filename.txt")

required_days_input = driver.find_element("id", "requiredDays")
required_days_input.clear()
required_days_input.send_keys("7")

redeemable_radio_yes = driver.find_element("css selector", "input[name='isRedeemable'][value='true']")
redeemable_radio_yes.click()


mrp_input = driver.find_element("id", "mrp")
mrp_input.send_keys("100")


loyalty_points_input = driver.find_element("id", "loyaltyPointsRequired")
loyalty_points_input.send_keys("10")

driver.find_element("id","fileId").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
time.sleep(1)

short_description = driver.find_element("id", "shortDescription")
short_description.send_keys("This is a short description.")

long_description = driver.find_element("id", "longDescription")
long_description.send_keys("This is a long description.")
time.sleep(2)

driver.find_element("xpath", "//button[text()='Save']").click()
time.sleep(5)

driver.find_element("id", "okbtn").click()
print("Offering CreatedSuccessfully")
time.sleep(2)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "assignedHealingsTable"))
)
offering_id_link = driver.find_element(By.XPATH, "//table[@id='assignedHealingsTable']/tbody/tr[2]/td[2]/a")
offering_id_link.click()
time.sleep(3)


driver.find_element(By.ID,"editBtn").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "i.bi.bi-pencil[style='position: absolute; right: 10px; z-index: 10;']").click()
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
time.sleep(2)
driver.find_element(By.ID,"fileName").send_keys("abd")
time.sleep(1)
driver.find_element("css selector", "div.col-sm-12.d-grid.p-0.my-4 > button.btn.btn-primary").click()
time.sleep(2)
driver.find_element("id", "close_error_message_moddle").click()
time.sleep(1)
driver.find_element(By.ID,"editBtn").click()
time.sleep(2)
input_field = driver.find_element(By.ID, "offeringName")
input_field.clear()
input_field.send_keys("Chakra Healing Session")


select_element = driver.find_element(By.ID, "editOfferingType")
select = Select(select_element)
select.select_by_visible_text("PRODUCT")

radio_button = driver.find_element(By.ID, "editIsRedeemable")
radio_button.click()

input_field = driver.find_element(By.ID, "loyaltyPointsRequired")
input_field.clear()
input_field.send_keys("500")

textarea = driver.find_element(By.ID, "editShortDescription")
textarea.clear()
textarea.send_keys("Updated text for short description.")

textarea = driver.find_element(By.ID, "editLongDescription")
textarea.clear()
textarea.send_keys("Updated text for long description.")
time.sleep(3)
driver.find_element(By.ID, "updateOfferingBtn").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[2]/div/button").click()
time.sleep(2)
print("Offering Updated successfulyy")
driver.find_element(By.ID,"deleteOfferingBtn").click()
time.sleep(1)
driver.find_element(By.ID,"confirm_delete_offering").click()
time.sleep(1)
driver.find_element(By.ID, "okbtn").click()
print(" Offering Deleted Successfully")

driver.quit()


