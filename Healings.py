import datetime
import random
import time

from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select

import databseConnection
from Functions import generate_random_date


def healings(driver):
    driver.get("http://185.199.53.169:5000/all-Healing-list")
    time.sleep(2)

    #----------------Sort----------------------------------------

    for i in range(2):
        driver.find_element(By.ID, "sortButton").click()
        time.sleep(2)
        print("Sorted")

    #----------------Filter--------------------------------------
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
    end_date_input.send_keys(Keys.ESCAPE)
    time.sleep(3)

    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "SELECT SUBSTRING(booking_id, 1, 5) AS booking_id FROM emis;"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = str(result[0][0]).zfill(5)
    print(customer_name)
    search_input = driver.find_element(By.ID, "bookingIdInput")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH, f"//div[@id='autocompleteList']//div[contains(text(), '{customer_name}')]").click()
    time.sleep(2)

    select_element = driver.find_element(By.ID, "HealerId")
    select = Select(select_element)
    options = select.options
    random_index = random.randint(1, len(options) - 1)
    random_option_text = options[random_index].text
    select.select_by_index(random_index)
    print(random_option_text)

    select_element = driver.find_element(By.NAME, "healingStatus")
    select = Select(select_element)
    options = select.options
    random_index = random.randint(1, len(options) - 1)
    random_option_text = options[random_index].text
    select.select_by_index(random_index)
    print(random_option_text)
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "a.text-decoration-none[href='/all-Healing-list']").click()
    time.sleep(3)
    print("Filter Successfully")

    #-----------------------------Edit----------------------------------------------
    cell = driver.find_element(By.XPATH, '//table[@id="leadsTable"]/tbody/tr[1]/td[2]/a')
    cell.click()
    time.sleep(5)

    see_booking_button = driver.find_element(By.CSS_SELECTOR, 'div.mt-0.ms-5 a.btn.btn-primary.btn-sm.ms-2')
    driver.execute_script("arguments[0].click();", see_booking_button)
    time.sleep(10)

    # Wait for page transition
    time.sleep(5)
    driver.get("http://185.199.53.169:5000/all-Healing-list")
    time.sleep(2)

    cell = driver.find_element(By.XPATH, '//table[@id="leadsTable"]/tbody/tr[1]/td[2]/a')
    cell.click()
    time.sleep(5)

    driver.find_element(By.ID, "editLeadBtn").click()
    select_element = driver.find_element(By.ID, "healingStatus")
    select = Select(select_element)
    options = select.options
    random_option = random.choice(options)
    select.select_by_visible_text(random_option.text)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    healing_instructions = [
        "Please ensure to drink plenty of water after the healing session.",
        "Rest for at least 30 minutes post-healing to maximize the effects.",
        "You might feel some discomfort for a few hours after the session, but it will subside.",
        "Avoid heavy physical activity for the next 24 hours.",
        "Apply the prescribed ointment twice a day for the next week."
    ]
    instruction_text = random.choice(healing_instructions)
    textarea = driver.find_element("id", "instructions")
    textarea.clear()
    textarea.send_keys(instruction_text)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")

    driver.find_element(By.ID, "saveChangesBtn").click()
    time.sleep(4)

    button = driver.find_element(By.ID, "global_Success_Message_Btn")
    button.click()
    print("Update successfully")

    driver.find_element("css selector", "a[href='/all-Healing-list']").click()  # get back to the healing screen
    time.sleep(3)

    #--------------------------Delete-----------------------------------------------------

    cell = driver.find_element(By.XPATH, '//table[@id="leadsTable"]/tbody/tr[1]/td[2]/a')
    cell.click()
    time.sleep(5)

    driver.find_element("css selector", "button[data-bs-target='#deleteModal']").click()
    time.sleep(2)

    driver.find_element("css selector", "#confirmDeleteButton").click()
    time.sleep(2)

    driver.find_element("css selector",
                        "#global_Success_Message_Model > div > div > div > div.row.mt-2.py-2.mb-2 > div > button").click()
    time.sleep(2)
    print("Delete Successfully")










