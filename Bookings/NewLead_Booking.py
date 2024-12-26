import random
import time
from datetime import datetime, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Functions import generate_random_description, generate_random_email, generate_random_name, \
    generate_unique_phone_number, generate_random_4_digit_time


def generate_random_dob(start_year=1950, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_dob = start_date + timedelta(days=random_days)
    return random_dob.strftime("%d-%m-%Y")

def newLead_Booking(driver):
    driver.get("http://185.199.53.169:5000/bookings")

    driver.find_element(By.XPATH, "//button[contains(text(), '+ Create New')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Free Booking')]").click()

    print("Clicked the Free Booking button successfully.")
    time.sleep(2)
    add_new_lead = driver.find_element(By.CSS_SELECTOR, 'span[data-bs-target="#New-Lead"]')
    driver.execute_script("arguments[0].click();", add_new_lead)
    time.sleep(3)
    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name = generate_random_name()
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name = generate_random_name()
    last_name_field.send_keys(last_name)

    phone_number = generate_unique_phone_number()
    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.send_keys(phone_number)

    email_field = driver.find_element(By.ID, "email")
    email = generate_random_email()
    email_field.send_keys(email)

    gender_radio_buttons = driver.find_elements(By.NAME, "Gender")
    random_choice = random.choice(gender_radio_buttons)
    random_choice.click()
    print(f"Selected Gender: {random_choice.get_attribute('value')}")

    dob_field = driver.find_element(By.ID, "dob")
    dob_field.clear()
    random_dob = generate_random_dob()
    dob_field.send_keys(random_dob)
    dob_field.send_keys(Keys.ESCAPE)

    select_element = driver.find_element(By.ID, "leadStatus")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)

    select_element = driver.find_element(By.ID, "leadSource")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)

    select_element = driver.find_element(By.ID, "country")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)

    select_element = driver.find_element(By.ID, "state")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)

    select_element = driver.find_element(By.ID, "city")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)
    print("city")
    time.sleep(2)

    address_field = driver.find_element(By.ID, "AddressLine_1")
    address = generate_random_name()
    address_field.send_keys(address)

    notes = driver.find_element(By.ID, "notes")
    notes_des = generate_random_description()
    notes.send_keys(notes_des)
    time.sleep(2)

    save_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Save')]")
    save_button.click()
    time.sleep(3)

    yes_button = driver.find_element(By.XPATH, "//button[@onclick='open_booking_model()']")
    yes_button.click()

    print("Successfully clicked the 'Yes' button.")
    print("New lead created")

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

    driver.find_element(By.CSS_SELECTOR,
                        "#FREE_booking > div > div > div.modal-footer.d-flex.justify-content-center.border.border-1 > div > div > button.btn.btn-primary.btn-sm").click()
    time.sleep(2)
    print("Free booking created")


    try:
        driver.find_element(By.ID, "global_Error_Message_Model").click()
        print("Click on error msg")
    except:
        driver.find_element(By.ID, "global_Success_Message_Model").click()
        print("Click on success msg")
    time.sleep(2)