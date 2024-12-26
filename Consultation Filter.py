
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import random
import string
import time


driver = webdriver.Chrome()

# Open the login page
driver.get("http://185.199.53.169:5000/login")  # Replace with your actual login URL

# Maximize the browser window (optional)
driver.maximize_window()

# Locate the username/email input field and enter the username/email
username_input = driver.find_element(By.ID, "username")  # Adjust ID for the actual field
username_input.send_keys("8788757703")

# Locate the password input field and enter the password
password_input = driver.find_element(By.ID, "password")  # Adjust ID for the actual field
password_input.send_keys("Admin@12345@")

# Optionally, wait for a couple of seconds
password_input.send_keys(Keys.RETURN)
time.sleep(2)
print(driver.current_url)
if "/dashboard" in driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")

time.sleep(2)

#Consultation Screen
#-----------------------------------------------------------
driver.get("http://185.199.53.169:5000/consultations")
time.sleep(2)
button = driver.find_element(By.CSS_SELECTOR, "#main-container > div:nth-child(1) > div.col-sm-12.rounded.d-flex.lead-head.mb-2 > div.col-sm-2.text-end.pe-1 > button:nth-child(2)")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(2)
#-----------------------------------------------------------------
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'search-input'))
)

# Type the search query into the search input
search_input.send_keys('Vishal Yadav')  # Replace with the name you're searching for

# Wait for the suggestions dropdown to appear
suggestions = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#dropdown-content div'))
    # Adjust the selector as needed
)

# If suggestions exist, proceed to select a random option
if suggestions:
    random_choice = random.choice(suggestions)

    # Scroll the random suggestion into view (to ensure it's clickable)
    driver.execute_script("arguments[0].scrollIntoView(true);", random_choice)

    # Click the random suggestion using JavaScript
    driver.execute_script("arguments[0].click();", random_choice)
#---------------------------------------------
WebDriverWait(driver, 5).until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, '.dropdown-item'))
)
dropdown_element = driver.find_element(By.ID, "filterRemedyType")

# Create a Select object
select = Select(dropdown_element)

# Define the two options
options = ["F2F", "ONLINE"]

# Randomly choose between the two options and select it
random_choice = random.choice(options)
select.select_by_visible_text(random_choice)

time.sleep(3)
dropdown_element = driver.find_element(By.ID, "filterMode")

# Create a Select object
select = Select(dropdown_element)

# Define the two options
options = ["Free", "Paid"]

# Randomly choose between the two options and select it
random_choice = random.choice(options)
select.select_by_visible_text(random_choice)

time.sleep(3)
#-------------------------------------------------
start_date_input = driver.find_element(By.ID, "filter-start-date")
start_date_input.click()

# Wait for the calendar to be visible and locate the date elements (adjust the selector to match the calendar structure)
calendar_dates = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#ui-datepicker-div'))  # Use the correct CSS selector for date elements
)

# Randomly select a date from the available dates
random_date = random.choice(calendar_dates)

# Scroll the date into view (if needed) and click it
driver.execute_script("arguments[0].scrollIntoView(true);", random_date)
random_date.click()
time.sleep(3)
#--------------------------------------------------
end_date_input = driver.find_element(By.ID, "filter-end-date")
end_date_input.click()

# Wait for the calendar to be visible and locate the date elements (adjust the selector to match the calendar structure)
calendar_dates = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#ui-datepicker-div'))  # Use the correct CSS selector for date elements
)

# Randomly select a date from the available dates
random_date = random.choice(calendar_dates)

# Scroll the date into view (if needed) and click it
driver.execute_script("arguments[0].scrollIntoView(true);", random_date)
random_date.click()
time.sleep(3)
#----------------------------------------------
button = driver.find_element(By.CSS_SELECTOR, "#filterConsultation > div > div.col-sm-8.d-flex.gap-3 > div.col-sm-3.d-flex > button.btn.btn-outline-primary.mt-4")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#------------------------------------------
button = driver.find_element(By.CSS_SELECTOR, "#filterResetConsultation")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#----------------------------------------------------

#-------------------------------------------------------------------------

driver.quit()