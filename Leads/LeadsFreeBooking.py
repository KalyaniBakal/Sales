
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import random
import string
import time

from Functions import generate_random_4_digit_time

driver = webdriver.Chrome()
#------------------Open login page-----------------------------
driver.get("http://185.199.53.169:5000/login")

#------------------- Maximize the browser window -----------------------
driver.maximize_window()
#----------------------------Enter username-----------------------
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("8788757703")

#----------------------Enter password--------------------------
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Admin@12345@")
password_input.send_keys(Keys.RETURN)
time.sleep(2)
#------------------------Redirect to dashboard------------------
print(driver.current_url)
if "/dashboard" in driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")

time.sleep(2)
#-------------------------------Marketing-Leads----------------------------
driver.get("http://185.199.53.169:5000/marketing-leads")
#-----------------Click on any random Lead-----------------------
leads = driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a")
if leads:
    random_lead = random.choice(leads)

    driver.execute_script("arguments[0].click();", random_lead)
else:
    print("No leads found on the page.")
time.sleep(3)
#---------------------Free booking----------------------------
free_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div/div[2]/button[2]")
free_button.click()
time.sleep(2)
#----------Function for starttime and endtime-----------


start_time_input = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "Start_timeInput")))
random_start_time = generate_random_4_digit_time()
start_time_input.clear()
start_time_input.send_keys(random_start_time)
time.sleep(4)

driver.execute_script("document.getElementById('start_time_pm').checked = true;")
driver.execute_script("document.getElementById('start_time_am').checked = true;")
end_time_input = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "End_timeInput")))
random_end_time = generate_random_4_digit_time()
end_time_input.clear()
end_time_input.send_keys(random_end_time)
driver.execute_script("document.getElementById('end_time_pm').checked = true;")
driver.execute_script("document.getElementById('end_time_am').checked = true;")
time.sleep(4)
#--------------Function for non-mandatory fields------------
def free_non_mandatory_fields():
    random_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ivy", "Jack"]
    random_name = random.choice(random_names)
    booking_field = driver.find_element(By.ID, "BookingFor")
    booking_field.clear()
    booking_field.send_keys(random_name)
    time.sleep(3)
#---------------------Generate random phone number-------------------
    random_phone_number = "+91" + str(random.choice([7, 8, 9])) + ''.join(random.choices("0123456789", k=9))

    giftee_phone_field = driver.find_element(By.ID, "GifteePhoneNo")
    giftee_phone_field.clear()
    giftee_phone_field.send_keys(random_phone_number)
    time.sleep(3)
#----------------Wish------------------
    health_wishes = [
        "Headache relief",
        "Lower blood pressure",
        "Stress reduction",
        "Improve sleep quality",
        "Relief from back pain",
        "Boost immunity",
        "Reduce anxiety",
        "Manage diabetes",
        "Improve digestion",
        "Enhance mental clarity"
    ]

    random_wish = random.choice(health_wishes)

    wish_field = driver.find_element(By.ID, "Wish")
    wish_field.clear()
    wish_field.send_keys(random_wish)
    time.sleep(3)
#-------------Referred by--------------------

#---------------Source------------------
    dropdown = Select(driver.find_element(By.ID, "Source"))

    options = ["OFFLINE", "ONLINE"]

    random_choice = random.choice(options)
    dropdown.select_by_visible_text(random_choice)
    time.sleep(3)


#-----------------------Save button--------------------------
def free_Submit():
   save_button = driver.find_element(By.XPATH, "/html/body/div[10]/div/div/form/div[2]/input[2]")
   save_button.click()
   time.sleep(2)

generate_random_4_digit_time()
free_non_mandatory_fields()
free_Submit()
#-------------------------------------
def edit_wish(new_wish):
    driver.find_element(By.NAME, "wish").send_keys(new_wish)

#------------------------------------------
Ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
Ok_button.click()
#-------------Sroll downwards---------------
driver.execute_script("window.scrollBy(0, 500);")  # Adjust the value as needed to scroll appropriately
time.sleep(3)
#----------------------------Click on Free booking tab-------------------
driver.find_element(By.ID, "free-booking-tab").click()
time.sleep(3)
#--------------------------------------------
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

edit_buttons = driver.find_elements(By.CLASS_NAME, "free-booking-edit-button")

# Check if any buttons are found
if edit_buttons:
    # Choose a random button and click
    random.choice(edit_buttons).click()
else:
    print("No edit buttons found on the page.")
time.sleep(3)
#-----------------------------------
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
#-------------------------------
edit_wish("Give Relief from Pain")
time.sleep(3)
#----------
save_buttons = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[6]/div/div[2]/div[1]/div/form/div[1]/div[2]/button[3]")

#---------------------------------
driver.quit()