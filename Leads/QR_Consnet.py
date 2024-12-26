import string
import time
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def QR(driver):
    driver.get("http://185.199.53.169:5000/marketing-leads")
    time.sleep(3)
    qr_code_button = driver.find_element(By.XPATH, "//button[contains(text(), 'QR Code')]")
    qr_code_button.click()
    time.sleep(2)
    # --------------------------------------
    link = driver.find_element(By.ID, "lead-form-link")
    link.click()

    driver.switch_to.window(driver.window_handles[1])

    time.sleep(2)
    # ---------------------------
    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.send_keys("Sumeet")
    last_name_field = driver.find_element(By.NAME, "lastName")  # Replace with actual 'name' attribute
    last_name_field.send_keys("Muley")
    # ---------------------Genearte random phone no-------------------------------
    random_phone = f"9{''.join([str(random.randint(0, 9)) for _ in range(9)])}"
    phone_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "phone"))
    )
    phone_input.clear()
    phone_input.send_keys(random_phone)
    time.sleep(3)
    # -------------------------Select lead status from dropdown--------------------------------
    driver.execute_script("document.querySelector('#leadStatus').click();")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/form/div[1]/div[4]/div[1]/select"))).click()
    time.sleep(2)
    # -------------------Select lead source from dropdown--------------------------------
    driver.execute_script("document.querySelector('#leadSource').click();")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/form/div[1]/div[4]/div[2]/select"))).click()
    time.sleep(2)

    # -----------------------Select country from dropdown-----------------------------
    driver.execute_script("document.querySelector('#country').click();")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/form/div[1]/div[5]/div[1]/select"))).click()
    time.sleep(2)

    # -------------------------Select state from dropdown-----------------------------
    state_dropdown = driver.find_element(By.ID, "state")

    select_state = Select(state_dropdown)

    # Get all options except the first one
    options = select_state.options[1:]

    # Choose a random option other than the first one and select it
    random_choice = random.choice(options)
    random_choice.click()
    time.sleep(3)
    # -------------------Select city from dropdown-----------------------------------
    city_dropdown = driver.find_element(By.ID, "city")

    select_city = Select(city_dropdown)

    options = select_city.options[1:]
    random_choice = random.choice(options)
    random_choice.click()
    # ---------------------Next----------------
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/button").click()
    # -----------------Success msg for Lead creation--------------------------
    driver.find_element(By.ID, "name").send_keys("John Doe")
    time.sleep(3)
    # -------------------------------------
    source_dropdown = driver.find_element(By.ID, "leadSource")

    select_source = Select(source_dropdown)

    # Get all options except the first one
    options = select_source.options[1:]

    # Choose a random option other than the first one and select it
    random_choice = random.choice(options)
    random_choice.click()
    time.sleep(3)
    # ------------------------------------------------
    driver.find_element(By.ID, "firstName").send_keys("Johnson Doe")
    time.sleep(3)
    # ------------------------------------------------------
    relationship_dropdown = driver.find_element(By.ID, "ecRelationship")

    select_relationship = Select(relationship_dropdown)

    # Get all options except the first one
    options = select_relationship.options[1:]

    # Choose a random option other than the first one and select it
    random_choice = random.choice(options)
    random_choice.click()
    time.sleep(3)
    # ------------------------------------------------------
    random_phone = f"9{''.join([str(random.randint(0, 9)) for _ in range(9)])}"
    phone_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ecWhatsappMob"))
    )
    phone_input.clear()
    phone_input.send_keys(random_phone)
    time.sleep(3)
    # ----------------------------------------------------------
    driver.find_element(By.ID, "servicesOfInterest").send_keys("helpNeededFromLovenheal")
    time.sleep(3)
    # -----------------------------------------------------------
    addresses = [
        "123 Main St, Springfield",
        "456 Oak Ave, Greenfield",
        "789 Pine Rd, Riverside",
        "101 Maple Dr, Lakewood",
        "202 Birch Ln, Hilltop"
    ]

    # Select a random address and enter it into the "Address" field
    random_address = random.choice(addresses)
    driver.find_element(By.ID, "notes").send_keys(random_address)
    time.sleep(3)
    # ----------------------------------------------------------------
    addresses = [
        "123 Main St, Springfield",
        "456 Oak Ave, Greenfield",
        "789 Pine Rd, Riverside",
        "101 Maple Dr, Lakewood",
        "202 Birch Ln, Hilltop"
    ]

    # Select a random address and enter it into the "Address" field
    random_address = random.choice(addresses)
    driver.find_element(By.NAME, "ecAddress").send_keys(random_address)
    time.sleep(3)
    # ------------------------------------------------------------------
    random_phone = f"9{''.join([str(random.randint(0, 9)) for _ in range(9)])}"
    phone_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "phone"))
    )
    phone_input.clear()
    phone_input.send_keys(random_phone)
    time.sleep(3)
    # ---------------------------------------------------------------------
    emails = [
        "user1@example.com",
        "test.email2@gmail.com",
        "sample.user3@yahoo.com",
        "info4@domain.com",
        "contact5@example.org"
    ]

    # Select a random email and enter it into the "Email" field
    random_email = random.choice(emails)
    driver.find_element(By.ID, "email").send_keys(random_email)
    time.sleep(3)
    # ----------------------------------------------------------------------
    driver.find_element(By.ID, "agreeToTermsYes").click()
    time.sleep(3)
    # ------------------------------------------------------------------------
    # driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[8]/div/label").click()
    # time.sleep(3)
    # ----------------------------------------------------------------------------
    file_input = driver.find_element(By.XPATH, "//*[@type='file']")
    file_input.send_keys("C:\\Users\\bakal\\OneDrive\\Desktop\\HC143.png")

    time.sleep(3)
    # --------------------------------------------------------------------------------
    button = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/button")

    driver.execute_script("arguments[0].click();",button)
    time.sleep(5)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-2])
    driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/button").click()
    time.sleep(15)
