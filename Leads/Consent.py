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

from logs import LoggingDriver
from dotenv import dotenv_values

config = dotenv_values('config.txt')

driver = webdriver.Chrome()
driver.maximize_window()
logging_driver = LoggingDriver(driver)  # Wrap the driver in the LoggingDriver

logging_driver.get("http://185.199.53.169:5000/login")

# Wait for username and password fields
WebDriverWait(logging_driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
WebDriverWait(logging_driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

# Find fields and fill in credentials using LoggingElement
username_field = logging_driver.find_element(By.ID, "username")
password_field = logging_driver.find_element(By.ID, "password")

username = config.get('username')
password = config.get('password')

username_field.send_keys(username)
password_field.send_keys(password + "\n")  # Press Enter

# Wait for login to process
time.sleep(2)

# Verify login success
if "/dashboard" in logging_driver.driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")
driver.get("http://185.199.53.169:5000/marketing-leads")
time.sleep(3)
lead = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, "/html/body/div[4]/div[3]/table/tbody/tr[1]/td[2]/a")))
driver.execute_script("arguments[0].click();", lead)
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

consent_tab = driver.find_element(By.ID, "consent-tab")
driver.execute_script("arguments[0].click();", consent_tab)
time.sleep(3)
# -----------------------------------------------
create_consent_button = driver.find_element(By.CSS_SELECTOR,
                                            "button.Consultation-history-btn.btn.btn-primary[data-bs-target='#Consent-QR']")

# Click the button
create_consent_button.click()
print("Consent form button clicked successfully!")
time.sleep(3)
# ----------------------------------------
link = driver.find_element(By.ID, "lead-form-link")
link.click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
# -------------------
driver.find_element(By.ID, "name").send_keys("John Doe")
time.sleep(3)
# -------------------------------------
source_dropdown = driver.find_element(By.ID, "leadSource")

select_source = Select(source_dropdown)

# Get all options except the first one
options = select_source.options[1:]

# Choose a random option other than the first one and select it
random_choice = random.choice(options)
random_choice.click()
time.sleep(3)
# ------------------------------------------------
driver.find_element(By.ID, "firstName").send_keys("Johnson Doe")
time.sleep(3)
# ------------------------------------------------------
relationship_dropdown = driver.find_element(By.ID, "ecRelationship")

select_relationship = Select(relationship_dropdown)

# Get all options except the first one
options = select_relationship.options[1:]

# Choose a random option other than the first one and select it
random_choice = random.choice(options)
random_choice.click()
time.sleep(3)
# ------------------------------------------------------
random_phone = f"9{''.join([str(random.randint(0, 9)) for _ in range(9)])}"
phone_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "ecWhatsappMob"))
)
phone_input.clear()
phone_input.send_keys(random_phone)
time.sleep(3)
# ----------------------------------------------------------
driver.find_element(By.ID, "servicesOfInterest").send_keys("helpNeededFromLovenheal")
time.sleep(3)
# -----------------------------------------------------------
addresses = [
    "123 Main St, Springfield",
    "456 Oak Ave, Greenfield",
    "789 Pine Rd, Riverside",
    "101 Maple Dr, Lakewood",
    "202 Birch Ln, Hilltop"
]

# Select a random address and enter it into the "Address" field
random_address = random.choice(addresses)
driver.find_element(By.ID, "notes").send_keys(random_address)
time.sleep(3)
# ----------------------------------------------------------------
addresses = [
    "123 Main St, Springfield",
    "456 Oak Ave, Greenfield",
    "789 Pine Rd, Riverside",
    "101 Maple Dr, Lakewood",
    "202 Birch Ln, Hilltop"
]

# Select a random address and enter it into the "Address" field
random_address = random.choice(addresses)
driver.find_element(By.NAME, "ecAddress").send_keys(random_address)
time.sleep(3)
# ------------------------------------------------------------------
random_phone = f"9{''.join([str(random.randint(0, 9)) for _ in range(9)])}"
phone_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "phone"))
)
phone_input.clear()
phone_input.send_keys(random_phone)
time.sleep(3)
# ---------------------------------------------------------------------
emails = [
    "user1@example.com",
    "test.email2@gmail.com",
    "sample.user3@yahoo.com",
    "info4@domain.com",
    "contact5@example.org"
]

# Select a random email and enter it into the "Email" field
random_email = random.choice(emails)
driver.find_element(By.ID, "email").send_keys(random_email)
time.sleep(3)
# ----------------------------------------------------------------------
driver.find_element(By.ID, "agreeToTermsYes").click()
time.sleep(3)
# ------------------------------------------------------------------------
# driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[8]/div/label").click()
# time.sleep(3)
# ----------------------------------------------------------------------------
file_path = r"C:/Users/bakal/OneDrive/Desktop/boy.jpeg"  # Replace with the actual file path

# Send the file path to the file input element
file_input = driver.find_element(By.XPATH, "//*[@type='file']")
file_input.send_keys(file_path)

# Optionally, wait for the file to upload
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
# --------------------------------------------------------------------------------
button = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/button")

driver.execute_script("arguments[0].click();",
                      button)
time.sleep(5)
# Get all window handles (tabs)
window_handles = driver.window_handles

# Switch to the previous tab (assuming there are at least 2 tabs open)
driver.switch_to.window(window_handles[-2])
time.sleep(3)
# -------------------------------------------
# button = driver.find_element(By.XPATH, "/html/body/div[16]/div/div/form/div[2]/button[1]")
#
# driver.execute_script("arguments[0].click();",
#                       button)  # filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.bg-white.text-primary
#
# time.sleep(5)
# # ------------------------------------

time.sleep(3)
# # ---------------

close_button = driver.find_element(By.CSS_SELECTOR, "button.btn-close.me-4[data-bs-dismiss='modal']")
driver.execute_script("arguments[0].click();", close_button)


print("Close button clicked successfully!")

time.sleep(3)
# -----------------
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

try:
    chevron_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-chevron-down.mx-3[href='#consent-1']")
    chevron_icon.click()
    print("Chevron icon clicked successfully!")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(3)
    chevron_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-chevron-down.mx-3[href='#consent-1']")
    driver.execute_script("arguments[0].click();", chevron_icon)
    time.sleep(3)


except Exception as e:
    print(f"Error: {e}")

finally:
    see_all_button = driver.find_element(By.CSS_SELECTOR, "#consent-all-btn.pointer.see-all-notactive")
    driver.execute_script("arguments[0].click();", see_all_button)
    time.sleep(3)
consent_button = driver.find_element(By.ID, "consent-latest-btn")
consent_button.click()
time.sleep(3)
