
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import random
import string
import time
from datetime import datetime, timedelta


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
#Consultations
#----------------------------------------------------
driver.get("http://185.199.53.169:5000/consultations")
time.sleep(2)
#--------------------------
button = driver.find_element(By.CSS_SELECTOR, "#main-container > div:nth-child(1) > div.col-sm-12.rounded.d-flex.lead-head.mb-2 > div.col-sm-2.text-end.pe-1 > button:nth-child(1)")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)

#-----------------------------------------------------
search_input = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, 'leadName')))
search_input.send_keys('Vishal Yadav')  # Replace with desired search query

# Wait for the dropdown with suggestions to appear
suggestions = WebDriverWait(driver, 10).until(
EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#leadNameDropdown .dropdown-item')))

if suggestions:
 random_choice = random.choice(suggestions)

 driver.execute_script("arguments[0].scrollIntoView(true);", random_choice)

 driver.execute_script("arguments[0].click();", random_choice)
 time.sleep(3)
else:
 print("No suggestions found!")

    #-------------Type------------
dropdown = Select(driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/form/div[1]/div[7]/div[2]/select"))

options = ["F2F", "ONLINE"]

random_choice = random.choice(options)
dropdown.select_by_visible_text(random_choice)
time.sleep(3)
#----------------------------------------------------------------
consultation_titles = [
     "Health Consultation with Specialist",
    "Mental Wellness Session",
    "Nutrition and Diet Advice",
    "Follow-up Consultation",
    "General Check-up",
    "Therapy Session",
    "Lifestyle Coaching Session",
    "Chronic Condition Management",
    "Personalized Health Assessment",
    "Stress Management Consultation"
]

random_title = random.choice(consultation_titles)

# Wait for the title input to be available
title_input = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, 'title')))

title_input.send_keys(random_title)
#--------------------------------------------------------------
chakra_checkboxes = [
    "crownCheckbox",
    "thirdeyeCheckbox",
    "throatcheckbox",
    "heartcheckbox",
    "solarplexuscheckbox",
    "sacralcheckbox",
    "rootcheckbox"
]

random_chakra = random.choice(chakra_checkboxes)

# Find the checkbox by ID and click it using JavaScript
chakra_checkbox = driver.find_element(By.ID, random_chakra)
driver.execute_script("arguments[0].click();", chakra_checkbox)
#----------------Notes---------
random_notes = [
        "This is the first random note.",
        "Important lead information.",
        "Follow up in a week.",
        "Need to review the details.",
        "Lead requires immediate attention."
    ]

note = random.choice(random_notes)

notes_field = driver.find_element(By.ID, "notes")
notes_field.clear()
notes_field.send_keys(note)
time.sleep(2)
#-------------------------------------------------------------
button = driver.find_element(By.CSS_SELECTOR, "#consultationForm > div.text-center.bg-body-secondary.py-3 > button.btn.btn-primary")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#-------------------------------------------------------------------
button = driver.find_element(By.CSS_SELECTOR, "#global_Success_Message_Model > div > div > div > div.row.mt-2.py-2.mb-2 > div > button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#--------------------------------------------------------------------
new_consultation = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[4]/table/tbody/tr[1]"))  # Adjust selector based on position or title
)

driver.execute_script("arguments[0].click();", new_consultation)
time.sleep(3)
#---------------------------------------------------------------------
button = driver.find_element(By.CSS_SELECTOR, "#individualconsultation_Edit")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#---------------------------------------------------------------------
random_phone = f"+919{''.join([str(random.randint(0, 9)) for _ in range(9)])}"

# Input the random phone number
phone_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "consultation_alternate_phoneNo"))
)
phone_input.clear()
phone_input.send_keys(random_phone)
time.sleep(3)
#----------------------------------------
dob = (datetime.now() - timedelta(days=random.randint(7300, 18250))).strftime("%d-%m-%Y")

# Locate the DOB input field
dob_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "consultation_dob"))
)

# Check if there is already a value in the DOB field
existing_dob = dob_input.get_attribute("value")

# If a DOB is already present, replace it with the new DOB
if existing_dob:
    print(f"Existing DOB found: {existing_dob}. Replacing it with new DOB: {dob}")
    dob_input.clear()

# Input the new DOB
dob_input.send_keys(dob)

# Simulate clicking outside the calendar to close it
body_element = driver.find_element(By.TAG_NAME, "body")
ActionChains(driver).move_to_element(body_element).click().perform()

time.sleep(3)
#------------------------
dropdown = Select(driver.find_element(By.ID, "consultation_remedyName"))

# Select a random option
random_option = random.choice(dropdown.options)
dropdown.select_by_visible_text(random_option.text)
time.sleep(3)
#-------------------------
dropdown = Select(driver.find_element(By.ID, "consultation_recommendedService"))

# Select a random option
random_option = random.choice(dropdown.options)
dropdown.select_by_visible_text(random_option.text)
time.sleep(3)
#----------------Save button----------------------
button = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/form/div[1]/div[2]/button[4]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#-------------------

#------------Confirmation msg---------------------------
button = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/div/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#----------------------------------------------------------------------
driver.quit()
