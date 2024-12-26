
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
"""
#--------------------------------Issues-------------------------
driver.get("http://185.199.53.169:5000/issues")
time.sleep(2)
#---------------------------------
button = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div[4]/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#----------------------------------------------------------
healer_name_input = driver.find_element(By.ID, "issueCustomerName")
healer_name_input.send_keys("Kalyani bakal")  # Replace with desired healer ID
time.sleep(3)
# Trigger the "Questions" dropdown by clicking on the input field
question_input = driver.find_element(By.ID, "question")
question_input.click()
# Wait for the dropdown options to appear and become visible
dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "questions-dropdown"))
)

# Ensure that the dropdown is visible and contains the options
dropdown_options = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#questions-list li"))
)

# Select a random question from the dropdown
if dropdown_options:
    random_option = random.choice(dropdown_options)
    random_option_text = random_option.text.strip()

    # Click on the selected random option
    random_option.click()
    print(f"Selected question: {random_option_text}")
time.sleep(3)
# Fill Comments
comments_input = driver.find_element(By.ID, "comments")
comments_input.send_keys("This is a sample issue.")  # Replace with your comments
time.sleep(3)
# Select Category
category_select = driver.find_element(By.ID, "category")
category_select.send_keys("INQUIRY")  # Replace with desired category
time.sleep(3)
# Select Priority
priority_select = driver.find_element(By.ID, "priority")
priority_select.send_keys("1")  # Replace with desired priority
time.sleep(3)
# ---------------------------------
button = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/form/div[2]/button[2]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)

button = driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div/div[4]/div/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#----------------------
new_issue = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/div[4]/table/tbody/tr[1]/td[2]"))  # Adjust selector based on position or title
)

driver.execute_script("arguments[0].click();", new_issue)
time.sleep(3)
#---------------Edit--------------------------------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div[1]/div[3]/div/button[3]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#--------------------------
dropdown = driver.find_element(By.ID, "category")

# Create a Select object
select = Select(dropdown)

# Get all available options
options = select.options

# Choose a random option
random_option = random.choice(options)

# Select the random option by visible text
select.select_by_visible_text(random_option.text)

print(f"Selected option: {random_option.text}")
time.sleep(3)
#----------------------------
radio_buttons = driver.find_elements(By.NAME, "userStatus")

# Choose a random radio button
random_radio = random.choice(radio_buttons)

# Click the selected radio button
random_radio.click()

# Print the value of the selected radio button
print(f"Selected radio button value: {random_radio.get_attribute('value')}")
#------------------------------------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/form/div[1]/div[3]/div/button[2]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#--------------------------------
button = driver.find_element(By.XPATH,"/html/body/div[7]/div/div/div/div[3]/div/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
"""
#--------------------Leads page-----------------------
driver.get("http://185.199.53.169:5000/marketing-leads")
time.sleep(2)
#----------------Detailed page------------------------------
lead = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[3]/table/tbody/tr[1]/td[2]/a")))
driver.execute_script("arguments[0].click();", lead)
time.sleep(3)
#--------------------------Issues tab------------------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/ul/li[6]")
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#-----------------------Create issue-------------------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[10]/div/div[1]/div[2]/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#--------------click on link-------------
link = driver.find_element(By.ID, "issue-form-link")
link.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
#------------------------new tab will open----------------
question_field = driver.find_element(By.ID, "question")
question_field.click()
options = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#questions-list li"))
)
random_option = random.choice(options)
random_option.click()
time.sleep(3)
#----------------------Image---------
file_input = driver.find_element(By.NAME, "file")
file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/boy.jpeg")
time.sleep(3)
#----------submit----------
button = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div/button[2]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#---------------switch to main pag---------------
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
#---------------close-----------------
button = driver.find_element(By.XPATH,"/html/body/div[20]/div/div/div/div[2]/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#------------------see all--------------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[10]/div/div[1]/div[2]/div[2]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#----------------expand------------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[10]/div/div[2]/div/div/div/form/div[1]/div[1]/i")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#------------------scroll-------------------
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
#--------------------edit-----------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[10]/div/div[2]/div/div/div/form/div[1]/div[2]/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#-----------changes-----------
textarea = driver.find_element(By.NAME, "comments")
random_comment = random.choice(["Great work!", "Needs improvement.", "Looking good!", "Please review this."])
textarea.send_keys(random_comment)
time.sleep(3)
#--------------------save button-------------------
button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[10]/div/div[2]/div/div/div/form/div[2]/div[12]/button[2]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
#----------------------Ok button---------------------
button = driver.find_element(By.XPATH,"/html/body/div[30]/div/div/div/div[3]/div/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)

driver.quit()