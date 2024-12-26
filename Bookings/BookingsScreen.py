
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

import databseConnection

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
#--------------------------------Category-------------------------
driver.get("http://185.199.53.169:5000/bookings")
time.sleep(3)
button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/button[2]")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
def generate_random_4_digit_time():
    hour = random.randint(0, 11)  # Random hour between 00 and 11 (12-hour format)
    minute = random.randint(0, 59)  # Random minute between 00 and 59
    return f"{hour:02d}{minute:02d}"

def paid_mandatory_field():
    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "select name from marketing_leads ;"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "Lead_name")
    search_input.send_keys(customer_name)
    time.sleep(5)
    dropdown_option_xpath = f"//div[@id='myDropdown-lead']//span[contains(text(), '{customer_name}')]"
    dropdown_option = driver.find_element(By.XPATH, dropdown_option_xpath)
    dropdown_option.click()
    time.sleep(2)

    driver.find_element(By.NAME, "totalAmount").send_keys(str(random.randint(100, 10000)))
    time.sleep(3)


def paid_non_mandatory_fields():


     #-------------giftee no
     random_phone_number = "+91" + str(random.choice([7, 8, 9])) + ''.join(random.choices("0123456789", k=9))

     giftee_phone_field = driver.find_element(By.ID, "gifteePhoneNo")
     giftee_phone_field.clear()
     giftee_phone_field.send_keys(random_phone_number)
     time.sleep(3)
     #-------------wish----------
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

     wish_field = driver.find_element(By.ID, "wish")
     wish_field.clear()
     wish_field.send_keys(random_wish)
     time.sleep(3)



     connection = databseConnection.conn()
     cursor = connection.cursor()
     cursor.execute("SELECT first_name FROM users")
     customer_name = cursor.fetchone()[0]

     try:
         search_input = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.ID, "ReferredBy"))
         )
         search_input.send_keys(customer_name)

         dropdown = WebDriverWait(driver, 10).until(
             EC.visibility_of_element_located((By.ID, "myDropdown"))
         )
         options = dropdown.find_elements(By.TAG_NAME, "span")
         time.sleep(3)
         if options:
             print(f"Found {len(options)} options in the dropdown.")
             random_option = random.choice(options)
             print(f"Selected option: {random_option.text}")
             random_option.click()
         else:
             print("No options found in the dropdown.")

     except Exception as e:
         print(f"Error interacting with dropdown: {e}")

     #----------Source----------
     dropdown = Select(driver.find_element(By.ID, "source"))

     options = ["OFFLINE", "ONLINE"]

     random_choice = random.choice(options)
     dropdown.select_by_visible_text(random_choice)
     time.sleep(3)


     """
     dropdown = Select(driver.find_element(By.ID, "healingMode"))

     options = ["SINGLE", "GROUP"]

     random_choice = random.choice(options)
     dropdown.select_by_visible_text(random_choice)
     time.sleep(3)
     """

     dropdown = Select(driver.find_element(By.ID, "offeringId"))
     options = dropdown.options
     random_choice = random.choice(options)
     dropdown.select_by_visible_text(random_choice.text)
     time.sleep(3)
     print(f"Selected: {random_choice.text}")

     start_date_input = driver.find_element(By.ID, "StartDate")
     start_date_input.click()

     calendar_dates = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#ui-datepicker-div')))

     random_date = random.choice(calendar_dates)

     driver.execute_script("arguments[0].scrollIntoView(true);", random_date)
     random_date.click()
     time.sleep(3)
     #--------------------
     end_date_input = driver.find_element(By.ID, "EndDate")
     end_date_input.click()

     calendar_dates = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#ui-datepicker-div'))
     )
     random_date = random.choice(calendar_dates)

     driver.execute_script("arguments[0].scrollIntoView(true);", random_date)
     random_date.click()
     time.sleep(3)

     created_date_input = driver.find_element(By.ID, "P_createdDate")
     created_date_input.click()

     calendar_dates = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[22]'))
     )
     random_date = random.choice(calendar_dates)

     driver.execute_script("arguments[0].scrollIntoView(true);", random_date)
     random_date.click()
     time.sleep(3)

     start_time_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Start_timeInput")))
     random_start_time = generate_random_4_digit_time()
     start_time_input.clear()
     start_time_input.send_keys(random_start_time)
     time.sleep(4)
     driver.execute_script("document.getElementById('start_time_am').checked = true;")
     driver.execute_script("document.getElementById('start_time_pm').checked = true;")
     end_time_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "End_timeInput")))
     random_end_time = generate_random_4_digit_time()
     end_time_input.clear()
     end_time_input.send_keys(random_end_time)
     driver.execute_script("document.getElementById('end_time_am').checked = true;")
     driver.execute_script("document.getElementById('end_time_pm').checked = true;")
     time.sleep(4)

     input_field = driver.find_element(By.ID, "requestedTimeInMins")
     random_duration = random.randint(1, 120)
     input_field.send_keys(str(random_duration))
     time.sleep(3)
     print(f"Random Call Duration Entered: {random_duration} minutes")

     dropdown = driver.find_element(By.ID, "coupon_code")
     dropdown.click()
     options = driver.find_elements(By.ID, "select_coupon")
     random_choice = random.choice(options)
     random_choice.click()
     time.sleep(5)
     button = driver.find_element(By.ID,"applyCouponButton")
     driver.execute_script("arguments[0].click();", button)
     time.sleep(3)

     random_instruction = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=50))
     textarea = driver.find_element(By.ID, "allottedInstructions")
     textarea.send_keys(random_instruction)
     time.sleep(3)
     print(f"Entered Instruction: {random_instruction}")



#-----------Save button-------
def submit():
    button = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[3]/div/div/button[2]")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    wait = WebDriverWait(driver, 10)
    try:
        ok_button = wait.until(EC.element_to_be_clickable((By.ID, "global_Success_Message_Btn")))
        ok_button.click()
        time.sleep(3)
    except:
        ok_button = wait.until(EC.element_to_be_clickable((By.ID, "global_Error_Message_Btn")))
        ok_button.click()
        time.sleep(3)

generate_random_4_digit_time()
def paidBooking(driver):
    paid_mandatory_field()
    paid_non_mandatory_fields()
    submit()


paidBooking(driver)