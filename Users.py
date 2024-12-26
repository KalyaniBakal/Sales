import random
import time
import databseConnection
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Functions import generate_random_name, generate_random_email


def generate_random_dob(start_year=1950, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_dob = start_date + timedelta(days=random_days)
    return random_dob.strftime("%d-%m-%Y")

connection = databseConnection.conn()
cursor = connection.cursor()

def users(driver):
    driver.get("http://185.199.53.169:5000/all-user-list")
    time.sleep(2)

    #--------------Filter--------------------------------------

    filter_icon = driver.find_element(By.CLASS_NAME, "bi-filter")
    filter_icon.click()
    time.sleep(3)

    query = "select first_name from users "
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "search_user_name")
    search_input.send_keys(customer_name)
    time.sleep(2)

    select_element = driver.find_element(By.ID, "status")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(2)

    select_element = driver.find_element(By.ID, "confirmed")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)

    select_element = driver.find_element(By.ID, "user_type")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Search')]").click()
    time.sleep(2)

    reset_link = driver.find_element(By.ID, "reloadBooking")
    reset_link.click()
    time.sleep(2)

    #--------------------Edit------------------------------------------------------------
    link = driver.find_element("xpath", "//tbody[@id='tableBody']/tr[1]/td[2]/a")
    link.click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "button#editLeadBtn.btn.btn-outline-primary.px-3").click()
    time.sleep(3)

    name = driver.find_element(By.ID, "fullname")
    name.clear()
    randomname = generate_random_name()
    name.send_keys(randomname)

    email = driver.find_element(By.NAME, "userEmail")
    email.clear()
    random_email = generate_random_email()
    email.send_keys(random_email)

    dob_field = driver.find_element(By.NAME, "userDob")
    dob_field.clear()
    random_dob = generate_random_dob()
    dob_field.send_keys(random_dob)

    radio_buttons = driver.find_elements(By.NAME, "userGender")
    random_radio_button = random.choice(radio_buttons)
    random_radio_button.click()
    time.sleep(3)

    select_element = driver.find_element(By.ID, "portalRole")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "button#saveChangesBtn").click()
    time.sleep(2)
    print("User updated successfully")





