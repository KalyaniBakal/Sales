from datetime import datetime
from lib2to3.pgen2.driver import Driver

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
# ------------------Open login page-----------------------------
driver.get("http://185.199.53.169:5000/login")

# ------------------- Maximize the browser window -----------------------
driver.maximize_window()
# ----------------------------Enter username-----------------------
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("8788757703")

# ----------------------Enter password--------------------------
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Admin@12345@")
password_input.send_keys(Keys.RETURN)
time.sleep(2)
# ------------------------Redirect to dashboard------------------
print(driver.current_url)
if "/dashboard" in driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")

time.sleep(2)
# -------------------------------Marketing-Leads----------------------------
driver.get("http://185.199.53.169:5000/marketing-leads")
# -----------------Click on any random Lead-----------------------
leads = driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a")
if leads:
    random_lead = random.choice(leads)

    driver.execute_script("arguments[0].click();", random_lead)
else:
    print("No leads found on the page.")
time.sleep(3)
# ---------------------Paid booking----------------------------
paid_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div/div[2]/button[3]")
paid_button.click()
time.sleep(2)


# ----------------starttime and end time
def generate_random_4_digit_time():
    hour = random.randint(0, 11)  # Random hour between 00 and 11 (12-hour format)
    minute = random.randint(0, 59)  # Random minute between 00 and 59
    return f"{hour:02d}{minute:02d}"




# --------------------------Mandatory fields----
def paid_mandatory_field():
    driver.find_element(By.NAME, "totalAmount").send_keys(str(random.randint(100, 10000)))
    time.sleep(3)

    coupon_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "coupon_code"))
    )

    # Click the input to trigger the dropdown
    coupon_input.click()

def paid_non_mandatory_fields():
    # random_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ivy", "Jack"]
    # random_name = random.choice(random_names)
    # booking_field = driver.find_element(By.ID, "P_BookingFor")
    # booking_field.clear()
    # booking_field.send_keys(random_name)
    # time.sleep(3)
    # # -------------giftee no
    # random_phone_number = "+91" + str(random.choice([7, 8, 9])) + ''.join(random.choices("0123456789", k=9))
    #
    # giftee_phone_field = driver.find_element(By.ID, "P_GifteePhoneNo")
    # giftee_phone_field.clear()
    # giftee_phone_field.send_keys(random_phone_number)
    # time.sleep(3)
    # # -------------wish----------
    # health_wishes = [
    #     "Headache relief",
    #     "Lower blood pressure",
    #     "Stress reduction",
    #     "Improve sleep quality",
    #     "Relief from back pain",
    #     "Boost immunity",
    #     "Reduce anxiety",
    #     "Manage diabetes",
    #     "Improve digestion",
    #     "Enhance mental clarity"
    # ]
    #
    # random_wish = random.choice(health_wishes)
    #
    # wish_field = driver.find_element(By.ID, "P_Wish")
    # wish_field.clear()
    # wish_field.send_keys(random_wish)
    # time.sleep(3)
    # # ----------Source----------
    # dropdown = Select(driver.find_element(By.ID, "P_Source"))
    #
    # options = ["OFFLINE", "ONLINE"]
    #
    # random_choice = random.choice(options)
    # dropdown.select_by_visible_text(random_choice)
    # time.sleep(3)
    #
    # # -----------------------Healing----
    # """
    # dropdown = Select(driver.find_element(By.ID, "P_HealingMode"))
    #
    # options = ["SINGLE", "GROUP"]
    #
    # random_choice = random.choice(options)
    # dropdown.select_by_visible_text(random_choice)
    # time.sleep(3)
    # """
    # # ----------start date----------
    #
    # start_time_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "P_Start_timeInput")))
    # random_start_time = generate_random_4_digit_time()
    # start_time_input.clear()
    # start_time_input.send_keys(random_start_time)
    # time.sleep(4)
    # driver.execute_script("document.getElementById('start_time_am1').checked = true;")
    # driver.execute_script("document.getElementById('start_time_pm1').checked = true;")
    # end_time_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "P_End_timeInput")))
    # random_end_time = generate_random_4_digit_time()
    # end_time_input.clear()
    # end_time_input.send_keys(random_end_time)
    # driver.execute_script("document.getElementById('end_time_am1').checked = true;")
    # driver.execute_script("document.getElementById('end_time_pm1').checked = true;")
    # time.sleep(4)
    #
    # start_date_input = driver.find_element(By.ID, "P_StartDate")
    # start_date_input.click()
    #
    # calendar_dates = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#ui-datepicker-div'))
    # )

    # random_date = random.choice(calendar_dates)

    # driver.execute_script("arguments[0].scrollIntoView(true);", random_date)
    # random_date.click()
    # time.sleep(3)
    # # --------------------
    # end_date_input = driver.find_element(By.ID, "P_EndDate")
    # end_date_input.click()
    #
    # calendar_dates = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#ui-datepicker-div'))
    # )
    # random_date = random.choice(calendar_dates)
    #
    # driver.execute_script("arguments[0].scrollIntoView(true);", random_date)
    # random_date.click()

    # try:
    #     # Wait for the dropdown menu to appear
    #     wait = WebDriverWait(driver, 10)
    #     driver.find_element(By.ID,"coupon_code").click()
    #     time.sleep(3)
    #     dropdown_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul#select_coupon")))
    #     time.sleep(3)
    #     # Find all coupon items in the dropdown
    #     coupon_items = dropdown_menu.find_elements(By.CLASS_NAME, "dropdown-item")
    #     time.sleep(3)
    #     random_item = random.choice(coupon_items)
    #     coupon_code = random_item.get_attribute("onclick").split("'")[1]
    #     time.sleep(3)
    #     random_item.click()
    #     print(f"Randomly Selected Coupon Code: {coupon_code}")


        try:
            # Wait for the dropdown input field
            wait = WebDriverWait(driver, 10)

            # Wait for the dropdown menu to appear (assumes options are in a list or menu)
            dropdown_menu = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu")))  # Replace with actual selector

            # Find all coupon options in the dropdown
            coupon_items = dropdown_menu.find_elements(By.CLASS_NAME, "dropdown-item")  # Update class if needed

            if coupon_items:
                # Randomly select one item
                random_item = random.choice(coupon_items)

                # Extract details (adjust selectors based on the structure of your dropdown items)
                coupon_code = random_item.text  # Assuming text contains the coupon code
                print(f"Randomly Selected Coupon Code: {coupon_code}")

                # Click the randomly selected coupon
                random_item.click()
            else:
                print("No coupons found in the dropdown.")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Ensure there are items to select
        # if coupon_items:
        #     # Randomly select one item
        #     random_item = random.choice(coupon_items)
        #
        #     # Extract details of the selected coupon
        #     coupon_code = random_item.get_attribute("onclick").split("'")[1]
        #     discount_details = random_item.find_element(By.CSS_SELECTOR, "div.col-sm-4 span:first-child").text
        #     description = random_item.find_element(By.CSS_SELECTOR, "div.col-sm-7 span").text
        #     print(f"Randomly Selected Coupon Code: {coupon_code}")
        #     print(f"Discount: {discount_details}, Description: {description}")
        #     random_item.click()
        #     print(f"Clicked on coupon: {coupon_code}")
        #
        # else:
        #     print("No coupons found in the dropdown.")
        # time.sleep(3)





# -----------Save button-------
def submit():
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[11]/div/div/form/div[2]/button[2]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)


# ------------------

paid_mandatory_field()
#paid_non_mandatory_fields()
#submit()


# -------------
def edit_wish(new_wish):
    driver.find_element(By.NAME, "wish").send_keys(new_wish)


# ____________
button = driver.find_element(By.XPATH,
                             "/html/body/div[28]/div/div/div/div[4]/div/button")  # Replace with the actual button's selector
driver.execute_script("arguments[0].click();", button)
time.sleep(3)
# ------------------
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
# -------------------------
driver.find_element(By.ID, "paid-booking-tab").click()
time.sleep(2)
# ---------------------Edit button-
edit_buttons = driver.find_elements(By.CLASS_NAME, "paid-booking-edit-button")

# Check if any buttons are found
if edit_buttons:
    # Choose a random button and click
    random.choice(edit_buttons).click()
else:
    print("No edit buttons found on the page.")
time.sleep(3)
# -----------Scroll
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
# ----------------------------

edit_wish("Give Relief from Pain")
time.sleep(3)
# ---Save changes----------
save_buttons = driver.find_elements(By.XPATH,
                                    "/html/body/div[4]/div/div[7]/div/div[2]/div[1]/div/form/div[1]/div[2]/button[3]")

driver.quit()
