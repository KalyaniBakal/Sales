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
feedback_tab = driver.find_element(By.ID, "feedback-tab")
driver.execute_script("arguments[0].click();", feedback_tab)
time.sleep(3)
# ------------------------------------------------------
button = driver.find_element(By.ID, "newFeedback")
button.click()
time.sleep(5)
#
# link = driver.find_element(By.ID, "feedback-form-link")
# link.click()
#
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(3)
# # -------------------------------------------------------
#
# random_star = random.randint(1, 5)
# print(f"Randomly selected star: {random_star}")
#
# star = driver.find_element(By.ID, f"star-{random_star}")
# star.click()
# print(f"{random_star}-star rating selected successfully!")
#
# feedback_value = driver.find_element(By.ID, "feedbackValue").get_attribute("value")
# print(f"Feedback value after rating: {feedback_value}")
#
# random_feedback = [
#     "This is a random feedback message.",
#     "I'm experiencing an issue with this.",
#     "Great experience so far!",
#     "This feature could use some improvement.",
#     "Looking forward to future updates."
# ]
#
# # Choose a random feedback message
# feedback_text = random.choice(random_feedback)
#
# # Locate the feedback textarea
# feedback_field = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME,"feedback"))
# )
# driver.execute_script("arguments[0].value = arguments[1];", feedback_field, feedback_text)
# time.sleep(3)
# # ---------------------------------------------------------
#
# file_path = r"C:/Users/bakal/OneDrive/Desktop/boy.jpeg"  # Replace with the actual file path
#
# # Send the file path to the file input element
# file_input = driver.find_element(By.XPATH, "//*[@type='file']")
# file_input.send_keys(file_path)
#
# # Optionally, wait for the file to upload
# time.sleep(3)
#
# submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
#
# submit_button.click()
# time.sleep(5)
# # ----------------------------------------------------------
# window_handles = driver.window_handles
#
# driver.switch_to.window(window_handles[-2])
# time.sleep(3)

close_button = driver.find_element(By.XPATH, "/html/body/div[19]/div/div/div/div[2]/button")

driver.execute_script("arguments[0].click();", close_button)
print("Close button clicked successfully!")
time.sleep(3)
# -----------------------Scroll-------------------------------------
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

try:
    chevron_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-chevron-down.mx-3[href='#feedback-1']")
    chevron_icon.click()
    print("Chevron icon clicked successfully!")
    edit_button = driver.find_element(By.CSS_SELECTOR, 'button.feedback-edit-button[data-target="#feedback-1"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
    edit_button.click()
    print("Edit button clicked successfully!")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    random_feedback = [
        "This is a random feedback message.",
        "I'm experiencing an issue with this.",
        "Great experience so far!",
        "This feature could use some improvement.",
        "Looking forward to future updates."
    ]
    feedback_text = random.choice(random_feedback)
    feedback_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,"feedback"))
    )
    feedback_field.clear()
    driver.execute_script("arguments[0].value = arguments[1];", feedback_field, feedback_text)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR,
                                      'button.feedback-save-button[data-target="#feedback-1"][data-issue-id="cb1b1bac-2826-4209-8cd1-e93c85fe7810"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    save_button.click()
    time.sleep(3)
    ok_button = driver.find_element(By.ID, 'global_Success_Message_Btn')
    driver.execute_script("arguments[0].scrollIntoView(true);", ok_button)
    ok_button.click()
    # chevron_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-chevron-down.mx-3[href='#feedback-1']")
    # driver.execute_script("arguments[0].click();", chevron_icon)
    # time.sleep(3)


except Exception as e:
    print(f"Error: {e}")

finally:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    see_all_button = driver.find_element(By.CSS_SELECTOR, "#feedback-all-btn.pointer.see-all-notactive")
    driver.execute_script("arguments[0].click();", see_all_button)
    time.sleep(3)
consent_button = driver.find_element(By.ID, "feedback-latest-btn")
consent_button.click()
time.sleep(3)
