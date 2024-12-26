import logging
import random
import datetime
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import databseConnection
from Functions import generate_random_date, random_name, generate_random_4_digit_time, generate_random_description, \
    generate_random_name, generate_future_date


def tasks(driver):
    driver.get("http://185.199.53.169:5000/tasks")
    time.sleep(2)
    #------------------Filters------------------------
    filter_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Filter')]")
    filter_button.click()

    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "SELECT title FROM tasks"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "search_task")
    search_input.send_keys(customer_name)

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

    time.sleep(2)
    select_element = driver.find_element(By.NAME, 'isRecurring')
    dropdown = Select(select_element)
    options = ["True", "False"]
    random_choice = random.choice(options)
    dropdown.select_by_value(random_choice)

    time.sleep(2)
    select_element = driver.find_element(By.NAME, 'status')
    dropdown = Select(select_element)
    options = ["OPEN", "CLOSED"]
    random_choice = random.choice(options)
    dropdown.select_by_value(random_choice)

    search_button = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
    search_button.click()
    time.sleep(4)

    #----------------Reset all ----------------------------------------------
    reset_link = driver.find_element(By.XPATH, "//a[text()='Reset all']")
    reset_link.click()
    time.sleep(4)

    #--------------Create Task-----------------------------------------------
    create_task_button = driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#new_task']")
    create_task_button.click()
    time.sleep(3)

    start_date = datetime.date(2024, 11, 1)
    end_date = datetime.date(2024, 12, 31)

    random_start_date = generate_future_date(start_date)
    random_end_date = generate_future_date(random_start_date)

    formatted_random_start_date = random_start_date.strftime("%d-%m-%Y")
    formatted_random_end_date = random_end_date.strftime("%d-%m-%Y")

    def tasks_mandatory_fields():
        random_name = generate_random_name()
        title = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/form/div[1]/div/input")
        title.send_keys(random_name)
        time.sleep(3)


        dueDate_input = driver.find_element(By.ID, "due_Date")
        dueDate_input.send_keys(formatted_random_start_date)


        time_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "timeInput")))
        random_start_time = generate_random_4_digit_time()
        time_input.clear()
        time_input.send_keys(random_start_time)
        time.sleep(4)
        selected_option = random.choice(["AM", "PM"])
        if selected_option == "AM":
            driver.execute_script("document.getElementById('time_am').checked = true;")
            print("Selected 'AM'")
        else:
            driver.execute_script("document.getElementById('time_pm').checked = true;")
            print("Selected 'PM'")


    def tasks_non_mandatory_fields():
        end_date_input = driver.find_element(By.ID, "end_Date")
        end_date_input.send_keys(formatted_random_end_date)


        false_radio = driver.find_element(By.ID, "flexRadioDefault1")
        true_radio = driver.find_element(By.ID, "flexRadioDefault2")
        selected_option = random.choice(["False", "True"])

        if selected_option == "False":
            false_radio.click()
            print("Selected 'False'")
        else:
            true_radio.click()
            print("Selected 'True'")
            time.sleep(3)
            recurrence_type_dropdown = Select(driver.find_element(By.ID, "recurrenceType"))
            recurrence_type_options = ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]
            selected_type = random.choice(recurrence_type_options)
            recurrence_type_dropdown.select_by_value(selected_type)
            print(f"Selected Recurrence Type: {selected_type}")

            if selected_type == "WEEKLY":
                days_button = driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#select_days']")
                days_button.click()

                time.sleep(1)
                days_checkboxes = driver.find_elements(By.NAME, "selected_days")
                num_days_to_select = random.randint(1, len(days_checkboxes))
                selected_days = random.sample(days_checkboxes, num_days_to_select)

                for checkbox in selected_days:
                    driver.execute_script("arguments[0].removeAttribute('disabled')", checkbox)
                    checkbox.click()
                    print(f"Selected Day: {checkbox.get_attribute('id')}")

        time.sleep(2)
        driver.find_element(By.NAME,"description").send_keys(generate_random_description())

    def tasks_submit():
        submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        print("Task Created")
        time.sleep(5)
        ok_button = driver.find_element(By.XPATH, "/html/body/div[10]/div/div/div/div[4]/div/button")
        ok_button.click()
        print("Click on OK button")
        logging.info("Task Created Successfully")
        time.sleep(3)

    tasks_mandatory_fields()
    tasks_non_mandatory_fields()
    tasks_submit()

    #---------------------Edit----------------------------------------------
    edit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Edit')]")
    edit_button.click()
    time.sleep(3)


    #--------------------Marked as Closed-----------------------------------
    close_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Mark as closed')]")
    close_button.click()
    time.sleep(3)
    yes_button = driver.find_element(By.ID, "yes_i_confirm")
    yes_button.click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[10]/div/div/div/div[3]/div/button").click()
    time.sleep(3)
    print("Marked as Closed")
    logging.info("Marked as Closed")

    #--------------------Delete---------------------------------------------
    delete_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]")
    delete_button.click()
    time.sleep(3)
    yes_button = driver.find_element(By.XPATH, "//button[text()='Yes']")
    yes_button.click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[3]/div/button").click()
    time.sleep(3)
    print("Deletd task successfully")
    logging.info("Deletd task successfully")
