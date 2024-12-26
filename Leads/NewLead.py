import random
import string
import time
from datetime import datetime, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from Functions import generate_random_name, generate_random_description, generate_random_email


def new_lead(driver):
    driver.get("http://185.199.53.169:5000/marketing-leads")
    time.sleep(3)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#New-Lead']"))
    )
    button.click()
    time.sleep(3)


    random_firstName = ["Vivek","Shri","Krishna","Alia","Priya","Amisha","Swara" ]
    firstName_text = random.choice(random_firstName)
    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.send_keys(firstName_text)

    random_lastName= ["Patil","Deshmukh","Kakde","Bakal","Sutar","Jadhav"]
    lastName_text = random.choice(random_lastName)
    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys(lastName_text)

    random_phone = f"9{''.join([str(random.randint(0, 9)) for _ in range(9)])}"
    phone_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "phone")) )
    phone_input.clear()
    phone_input.send_keys(random_phone)
    time.sleep(3)

    email_field = driver.find_element(By.ID, 'email')
    random_email = generate_random_email()
    email_field.send_keys(random_email)

    random_Gender = ["MALE", "FEMALE", "SPECIAL"]
    Gender_text = random.choice(random_Gender)
    driver.find_element(By.ID, Gender_text).click()
    time.sleep(2)

    def generate_random_dob(start_year=1950, end_year=2005):
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31)
        random_days = random.randint(0, (end_date - start_date).days)
        random_dob = start_date + timedelta(days=random_days)
        return random_dob.strftime("%d-%m-%Y")

    dob_field = driver.find_element(By.ID, 'dob')
    random_dob = generate_random_dob()
    dob_field.send_keys(random_dob)


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


    success_message = driver.find_element(By.ID, "global_Success_Message").text
    print("Success Message:", success_message)


    if "Leads" in driver.title:
        print("Lead has been successfully created.")
    else:
        print("Failed to create lead.")
    time.sleep(3)