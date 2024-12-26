import datetime
import logging
import random
import string
import time
import databseConnection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Functions import generate_random_date


def generate_random_text(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))
random_text = generate_random_text(100)


def calls(driver):
    driver.get("http://185.199.53.169:5000/calls")
    logging.info("Navigating to Call Screen")
    time.sleep(2)
    # --------------Sort---------------------------------------
    for i in range(2):
        sort_button = driver.find_element(By.ID, "sortButton")
        sort_button.click()
        #print("Sort button clicked.")

        time.sleep(3)
    logging.info("Sorting Successfully.")
    # ---------------------Filter-------------------------------------------------------

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
    logging.info("Start date: " + formatted_random_start_date)
    logging.info("End date: " + formatted_random_end_date)

    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "select name from marketing_leads "
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.NAME, "customerName")
    search_input.send_keys(customer_name)
    time.sleep(3)
    logging.info("Enter Customer Name")

    query = "select caller_name from sales_calls"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.NAME, "callerName")
    search_input.send_keys(customer_name)
    time.sleep(5)
    logging.info("Enter Caller Name")

    dropdown = driver.find_element(By.ID, "calledStatus")
    select = Select(dropdown)
    options = [option.get_attribute("value") for option in select.options if option.get_attribute("value")]
    random_option = random.choice(options)
    select.select_by_value(random_option)
    time.sleep(3)
    logging.info("Enter Called Status")

    # Locate the button using partial match
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()
    print("Search button clicked.")
    logging.info("Filter Successfully ")
    time.sleep(3)

    reset_button = driver.find_element(By.ID, "reset")
    reset_button.click()
    print("Reset button clicked.")
    logging.info("Click on Reset all button ")
    time.sleep(3)

    # -------------Create Call--------------------------------------------

    call_button = driver.find_element(By.ID, "addNewCall")
    call_button.click()
    print("Click on Add New Call")
    logging.info("Click on Add New Call")
    time.sleep(2)

    query = "select name from marketing_leads "
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.NAME, "customerName")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH, f"//ul[@id='lead_data']//li[contains(text(), '{customer_name}')]").click()
    print("Select name from the marketing lead")
    logging.info("Select name from the marketing lead")

    call_duration_field = driver.find_element(By.NAME, "callDuration")
    call_duration_field.send_keys(random.randint(0, 90))
    print("Enter duration ")
    logging.info("Enter duration ")

    notes_field = driver.find_element(By.NAME, "Notes")
    notes_field.send_keys(random_text)
    print("Enter Notes")
    logging.info("Enter Notes")

    add_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm.px-4")
    add_button.click()
    print("Clicked on the Add button")
    logging.info("Call Created Successfully")
    # 10. **Click 'Cancel' Button (Optional)**
    # cancel_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-secondary.btn-sm.px-3")
    # cancel_button.click()
    # print("Clicked on the Cancel button")

    time.sleep(2)

    driver.execute_script("document.querySelector('button[data-bs-dismiss=\"modal\"]').click()")
    print("Clicked on the OK button")
    time.sleep(2)
    driver.execute_script("document.querySelector('i.bi.bi-chevron-left').click()")
    # -------------Edit --------------------------
    driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[2]/a").click()
    logging.info("Navigate to call detail screen")

    edit_button = driver.find_element(By.ID, "Edit_call")
    edit_button.click()
    logging.info("Click on edit button")

    call_duration_field = driver.find_element(By.NAME, "callDuration")
    call_duration_field.clear()
    duration = random.randint(0, 90)
    call_duration_field.send_keys(random.randint(0, 90))
    print("Duration updated")
    logging.info("Update Duration")

    notes_field = driver.find_element(By.NAME, "Notes")
    notes_field.clear()
    notes_field.send_keys(random_text)
    print("Notes updated")
    logging.info("Update Notes")

    update_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-sm.px-3[type="submit"]')
    update_button.click()
    logging.info("Updated Successfully")
    logging.info("Click on delete button")
    logging.info("Call deleted successfully")

    driver.execute_script("document.querySelector('button[data-bs-dismiss=\"modal\"]').click()")
    print("Edit successfully")

    #driver.execute_script("document.querySelector('i.bi.bi-chevron-left').click()")




