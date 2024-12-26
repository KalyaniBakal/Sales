import random
import time
import databseConnection
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Functions import generate_random_date


def generate_random_dob(start_year=1950, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_dob = start_date + datetime.timedelta(days=random_days)
    return random_dob.strftime("%d-%m-%Y")

connection = databseConnection.conn()
cursor = connection.cursor()

def top_Customers(driver):
    driver.get("http://185.199.53.169:5000/top-customers-report")
    time.sleep(2)

    #--------------Filter--------------------------------------

    filter_icon = driver.find_element(By.ID, "filterBtn")
    filter_icon.click()
    time.sleep(3)

    query = "select booking_for from bookings;"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.NAME, "search-name")
    search_input.send_keys(customer_name)
    time.sleep(2)
    driver.find_element(By.XPATH,f"//div[@id='dropdown-content']//div[contains(text(), '{customer_name}')]").click()
    time.sleep(2)

    select_element = driver.find_element(By.ID, "type")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options[1:])
    select.select_by_visible_text(random_option.text)
    time.sleep(2)

    start_date = datetime.date(2024, 11, 1)  # Example start date
    end_date = datetime.date(2024, 12, 31)  # Example end date
    random_start_date = generate_random_date(start_date, end_date)
    random_end_date = generate_random_date(random_start_date, end_date)
    formatted_random_start_date = random_start_date.strftime("%d-%m-%Y")
    formatted_random_end_date = random_end_date.strftime("%d-%m-%Y")
    start_date_input = driver.find_element(By.ID, "startDate")
    end_date_input = driver.find_element(By.ID, "endDate")
    start_date_input.send_keys(formatted_random_start_date)
    end_date_input.send_keys(formatted_random_end_date)
    print("Start date: " + formatted_random_start_date)
    print("End date: " + formatted_random_end_date)

    driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Search')]").click()
    time.sleep(2)

    reset_link = driver.find_element(By.ID, "resetButton")
    reset_link.click()
    time.sleep(2)

    #-----------------Edit----------------------------------------
    cell = driver.find_element(By.CSS_SELECTOR, "#leadsTable tbody tr:nth-child(1) td:nth-child(2)")
    cell.click()
    time.sleep(2)
