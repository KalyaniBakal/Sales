import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from Functions import generate_random_4_digit_time
from utility.database import fetch_customer_names
from utility.logs import LoggingDriver
from selenium.webdriver.support.ui import Select
def click_new_healer_button(driver):
    """
    Clicks the 'New Healer' button on the page.
    """
    try:
        # Wait for the button to be clickable
        new_healer_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#new_healer']"))
        )
        new_healer_button.click()
        print("Clicked 'New Healer' button.")
    except Exception as e:
        print(f"Error clicking 'New Healer' button: {e}")

def populate_customer_name_field(driver, customer_name):
    """
    Populates the 'Customer Name' field with the given name and selects the corresponding option from the dropdown.
    """ 
    
        # Wait for the input field to appear
    customer_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "healer_name"))
    )
    customer_name_field.clear()  # Clear any existing text
    customer_name_field.send_keys(customer_name) 
    print(f"Populated 'Customer Name' field with: {customer_name}")
    time.sleep(4)
    dropdown_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#Dropdown .ps-2.py-1'))
    )
    if dropdown_items:
        random_choice = random.choice(dropdown_items)

        driver.execute_script("arguments[0].scrollIntoView(true);", random_choice)

        driver.execute_script("arguments[0].click();", random_choice)
        time.sleep(3)
    print(f"Selected suggestion for: {customer_name}")
    time.sleep(1)
    print(f"Populated 'Customer Name' field with: {customer_name}") 

def add_new_healer(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/getHealers")
    time.sleep(3)

    try:
        # Fetch customer names from the database
        customer_names = fetch_customer_names()
        if not customer_names:
            print("No customer names found in the database.")
            return
        click_new_healer_button(driver)
        populate_customer_name_field(driver, customer_names)
        
        # Populate experience in months with random data
        experience_in_months = random.randint(1, 36)
        experience_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "experienceInMonths"))
        )
        experience_field.clear()
        experience_field.send_keys(experience_in_months)
        print(f"Populated 'Experience in Months' field with: {experience_in_months}")
        time.sleep(2)

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


        healing_minutes = random.randint(0, 59)
        healing_minutes_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "healingTimeMins"))
        )
        healing_minutes_field.clear()
        healing_minutes_field.send_keys(healing_minutes)
        print(f"Populated 'healingTimeMins' field with: {healing_minutes}")
        time.sleep(2)
       
        healingsPerDay = random.randint(0, 59)
        healingsPerDay_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "healingsPerDay"))
        )
        healingsPerDay_field.clear()
        healingsPerDay_field.send_keys(healingsPerDay)
        print(f"Populated 'healingsPerDay' field with: {healingsPerDay}")
        time.sleep(2)

        dropdown = Select(driver.find_element(By.ID, "isDistressedHelplineMember"))
        selected_value = random.choice(["true", "false"])
        dropdown.select_by_value(selected_value)
        print(f"Selected value in dropdown: {selected_value}")
        time.sleep(2)
        
        # Automatic Payout
        dropdown_automatic_payout = Select(driver.find_element(By.ID, "automaticPayout"))
        automatic_payout_value = random.choice(["true", "false"])
        dropdown_automatic_payout.select_by_value(automatic_payout_value)
        print(f"Selected 'Automatic Payout': {automatic_payout_value}")
        time.sleep(2)

        # Is Inactive
        dropdown_is_inactive = Select(driver.find_element(By.ID, "isInactive"))
        is_inactive_value = random.choice(["true", "false"])
        dropdown_is_inactive.select_by_value(is_inactive_value)
        print(f"Selected 'Is Inactive': {is_inactive_value}")
        time.sleep(2)

        # Plan
        dropdown_plan = Select(driver.find_element(By.ID, "plan"))
        plan_value = random.choice(["FREE", "PREMIUM", "LOVENHEAL"])
        dropdown_plan.select_by_value(plan_value)
        print(f"Selected 'Plan': {plan_value}")
        time.sleep(2)

        # Data Verified
        dropdown_data_verified = Select(driver.find_element(By.ID, "dataVerified"))
        data_verified_value = random.choice(["true", "false"])
        dropdown_data_verified.select_by_value(data_verified_value)
        print(f"Selected 'Data Verified': {data_verified_value}")
        time.sleep(2)

        # Healer Rank
        dropdown_healer_rank = Select(driver.find_element(By.ID, "healerRank"))
        healer_rank_value = str(random.randint(1, 10))  # Random rank between 1 and 10
        dropdown_healer_rank.select_by_value(healer_rank_value)
        print(f"Selected 'Healer Rank': {healer_rank_value}")
        time.sleep(2)

        # Healing Level
        dropdown_healing_level = Select(driver.find_element(By.ID, "healingLevel"))
        healing_level_value = random.choice(["LEVEL1", "LEVEL2", "LEVEL3"])
        dropdown_healing_level.select_by_value(healing_level_value)
        print(f"Selected 'Healing Level': {healing_level_value}")
        time.sleep(2)

        # Data Verification Stage
        dropdown_data_verification_stage = Select(driver.find_element(By.ID, "dataVerificationStage"))
        data_verification_stage_value = random.choice([
            "NOT_INITIATED", "INITIATED", "VERIFICATION_PENDING", 
            "VERIFICATION_HOLD", "VERIFICATION_REJECTED", "VERIFIED"
        ])
        dropdown_data_verification_stage.select_by_value(data_verification_stage_value)
        print(f"Selected 'Data Verification Stage': {data_verification_stage_value}")
        time.sleep(2)

        dropdown_id = "selectBox"
        options_container_id = "optionsList"
        dropdown = driver.find_element(By.ID, dropdown_id)
        dropdown.click()
        time.sleep(2)  # Allow dropdown to expand

        # Locate all options in the dropdown
        options = driver.find_elements(By.CSS_SELECTOR, f"#{options_container_id} .option")

        if not options:
            raise Exception("No options found in the dropdown.")

        if len(options) < 10:
            raise ValueError("Requested number of options exceeds available options.")

        # Randomly select options
        selected_options = random.sample(options, 10)

        for option in selected_options:
            option.click()  # Click to select the option
            print(f"Selected option: {option.text.strip()}")
            time.sleep(1)  # Pause between selections for clarity

        # Optionally close the dropdown by clicking outside or on the dropdown again
        dropdown.click()
        
        time.sleep(1)
        # Locate the short bio input field
        short_bio = driver.find_element(By.ID, "shortBio")
        short_bio.clear()  # Clear any existing text
        short_bio.send_keys("This is a short bio of the healer.")  # Enter the short bio

        # Locate the long bio textarea
        long_bio = driver.find_element(By.ID, "longBio")
        long_bio.clear()  # Clear any existing text
        long_bio.send_keys("This is a detailed and comprehensive bio of the healer, describing their experience, methods, and specialties.")  # Enter the long bio

        # Optional: Verify the entered text
        print("Short Bio:", short_bio.get_attribute("value"))
        print("Long Bio:", long_bio.get_attribute("value"))

        
        save_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm.px-3")
        save_button.click()
        time.sleep(2)  # Adjust the sleep time as needed

        try:
            ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
            ok_button.click()
            time.sleep(3)
        except:
            ok_button = driver.find_element(By.ID, "global_Error_Message_Btn")
            ok_button.click()
            time.sleep(3)

    except Exception as e:
        print(f"Error in adding new healer: {e}")

def edit_healer(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/getHealers")
    time.sleep(3)
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#table_body tr")
    random_row = random.choice(table_rows)
    random_row.click()
    
    # Optional: Wait for the page to load after clicking
    time.sleep(2)
    # Find and click the "Edit" button to open the edit form
    edit_button = driver.find_element(By.ID, "editHealer")
    edit_button.click()
    time.sleep(2)  # Wait for the edit form to load

    # Edit the "No Disturb Start Time"
    no_disturb_start_time_input = driver.find_element(By.ID, "noDisturbStartTime")
    no_disturb_start_time_input.clear()  # Clear the existing value
    no_disturb_start_time_input.send_keys("11:00 AM")  # Set the new time
    time.sleep(2)

    # Edit the "No Disturb End Time"
    no_disturb_end_time_input = driver.find_element(By.ID, "noDisturbEndTime")
    no_disturb_end_time_input.clear()  # Clear the existing value
    no_disturb_end_time_input.send_keys("12:00 PM")  # Set the new time
    time.sleep(2)

    # Edit the "Healer Rank"
    healer_rank_input = driver.find_element(By.NAME, "healerRank")
    healer_rank_input.clear()  # Clear the existing value
    healer_rank_input.send_keys("1.2")  # Set the new healer rank
    time.sleep(2)

    # Edit the "Healings Per Day"
    healings_per_day_input = driver.find_element(By.NAME, "healingsPerDay")
    healings_per_day_input.clear()  # Clear the existing value
    healings_per_day_input.send_keys("30")  # Set the new healings per day
    time.sleep(2)
    healing_time_input = driver.find_element(By.NAME, "healingTimeMins")
    healing_time_input.clear()  # Clear the existing value
    healing_time_input.send_keys("16")  # Set the new healing time
    time.sleep(2)

    # Edit the "Experience in Months"
    experience_months_input = driver.find_element(By.NAME, "experienceInMonths")
    experience_months_input.clear()  # Clear the existing value
    experience_months_input.send_keys("2")  # Set the new experience in months
    time.sleep(2)


    # Optionally, click a "Save" or "Submit" button if needed
    # submit_button = driver.find_element(By.ID, "submitHealer")
    # submit_button.click()
    # time.sleep(2)
