import time

from faker.generator import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def address(driver):
    driver.get("http://185.199.53.169:5000/static/get_all_address")
    time.sleep(2)

    # ---------------------------------Addresss Filter------------------------------

    button = driver.find_element(By.CSS_SELECTOR,
                                 "#main-container > div.col-12.bg-white.rounded.d-flex.p-2 > div.col-sm-2.d-flex.justify-content-end.align-items-center > div > button:nth-child(2)")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -----------------Search by name------------
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'user_name'))
    )

    search_input.send_keys('Kalyani Bakal')  # Replace with the name you're searching for

    suggestions = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#myDropdown'))
    )

    if suggestions:
        random_choice = random.choice(suggestions)

        driver.execute_script("arguments[0].scrollIntoView(true);", random_choice)

        driver.execute_script("arguments[0].click();", random_choice)

        driver.execute_script("document.querySelector('body').click();")

    else:
        print("No suggestion found")
        time.sleep(3)
    # ---------------City------------------------
    dropdown_element = driver.find_element(By.ID, "city_f")

    select = Select(dropdown_element)

    all_options = select.options

    available_options = [option.text for option in all_options if option.text]

    random_choice = random.choice(available_options)

    select.select_by_visible_text(random_choice)

    print(f"Randomly selected option: {random_choice}")
    time.sleep(3)
    # -----------------------State----------------------------------
    dropdown_element = driver.find_element(By.ID, "state_f")

    select = Select(dropdown_element)

    all_options = select.options

    available_options = [option.text for option in all_options if option.text]

    random_choice = random.choice(available_options)

    select.select_by_visible_text(random_choice)

    print(f"Randomly selected option: {random_choice}")
    time.sleep(3)
    # ---------------------Country------------------------------------------
    country_dropdown = Select(driver.find_element("id", "country_f"))
    country_dropdown.select_by_visible_text("India")
    time.sleep(3)
    # ----------------Search button--------------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#Filter_address > div > div.col-sm-3.mt-4 > button")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -------------------Reset button--------------------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#Filter_address > div > div.col-sm-3.mt-4 > a")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)

    # -------------------------------Add New Address---------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#main-container > div.col-12.bg-white.rounded.d-flex.p-2 > div.col-sm-2.d-flex.justify-content-end.align-items-center > div > button:nth-child(1)")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # ----------------------Add name-----------------------------------------
    search_input = driver.find_element(By.ID, "search")
    search_input.send_keys("Amisha Jadhav")
    time.sleep(2)

    dropdown_options = driver.find_elements(By.CSS_SELECTOR, "#myDropdown1 span")
    if dropdown_options:
        random.choice(dropdown_options).click()
    else:
        print("No options found in the dropdown")
    time.sleep(3)
    # ---------------------Flat no--------------------------------------------
    flat_number = random.randint(1, 100)
    building_name = f"Building {chr(random.randint(65, 90))}"

    address_input = driver.find_element(By.ID, "flatNoBuildingName")
    address_input.send_keys(f"Flat {flat_number}, {building_name}")

    time.sleep(3)
    # ---------------------------Locality----------------------------------------
    locality = f"Locality {random.randint(1, 100)}"
    street = f"Street {chr(random.randint(65, 90))}"

    locality_area_input = driver.find_element(By.ID, "localityAreaStreet")
    locality_area_input.send_keys(f"{locality}, {street}")

    time.sleep(3)
    # ----------------------------Country-----------------------------------------
    country_dropdown = Select(driver.find_element("id", "country"))

    options = country_dropdown.options[1:]  # Exclude the "Select Country" option
    random_country = random.choice(options)

    country_dropdown.select_by_visible_text(random_country.text)
    time.sleep(5)
    # ---------------------------State---------------------------------------------
    state_dropdown = Select(driver.find_element("id", "state"))

    options = state_dropdown.options[1:]  # Exclude the "Select Country" option
    random_state = random.choice(options)

    state_dropdown.select_by_visible_text(random_state.text)
    time.sleep(5)
    # -----------------------City------------------------------------------------------
    city_dropdown = Select(driver.find_element("id", "city"))

    options = city_dropdown.options[1:]  # Exclude the "Select Country" option
    random_city = random.choice(options)

    city_dropdown.select_by_visible_text(random_city.text)
    time.sleep(5)
    # -----------------------------------Postal code--------------------------------------------
    postal_code = str(random.randint(100000, 999999))

    postal_code_input = driver.find_element("id", "postalCode")
    postal_code_input.send_keys(postal_code)

    print(f'Entered Postal Code: {postal_code}')

    # Pause for a moment to observe the input (optional)
    time.sleep(3)
    # --------------------------------------Save Address button------------------------------------------------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#create_new_address > div > div > div.modal-footer.d-flex.justify-content-center.border.border-1 > div > div > button.btn.btn-primary.btn-sm")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -------------------------------Confirmatipon button-------------------------------------------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[10]/div/div/div/div[4]/div/button")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # --------------------------------------------------------------------------------------------

    address_links = driver.find_elements(By.CSS_SELECTOR, "td > a.text-decoration-none")
    random.choice(address_links).click()
    time.sleep(3)
    # -----------------Edit button---------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div[3]/ul/li[1]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # ----------------------Country-------------------
    country_dropdown = Select(driver.find_element("id", "country"))

    # Get all options, choose a random one (skipping the first default option)
    options = country_dropdown.options[1:]  # Exclude the "Select Country" option
    random_country = random.choice(options)

    # Select the random country
    country_dropdown.select_by_visible_text(random_country.text)
    time.sleep(5)
    # ----------------State--------------------
    state_dropdown = Select(driver.find_element("id", "state"))

    # Get all options, choose a random one (skipping the first default option)
    options = state_dropdown.options[1:]  # Exclude the "Select Country" option
    random_state = random.choice(options)

    # Select the random country
    state_dropdown.select_by_visible_text(random_state.text)
    time.sleep(5)
    # ------------------City-------------------------
    city_dropdown = Select(driver.find_element("id", "city"))

    # Get all options, choose a random one (skipping the first default option)
    options = city_dropdown.options[1:]  # Exclude the "Select Country" option
    random_city = random.choice(options)

    # Select the random country
    city_dropdown.select_by_visible_text(random_city.text)
    time.sleep(5)
    # ------------------------------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div[2]/button")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # --------------------------------------------------

    button = driver.find_element(By.XPATH,
                                 "/html/body/div[8]/div/div/div/div[3]/div/button")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)

    # ----------------------Delete-----------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div[3]/ul/li[2]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -------------------------Confirmation msg--------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[11]/div/div/div/div[2]/div/button[1]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)

    # ---------------------------------------------------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[1]/div[2]/div/a")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)



