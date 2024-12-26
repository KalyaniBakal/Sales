import time

from faker.generator import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def category(driver):
    driver.get("http://185.199.53.169:5000/static/category/get_all_category")
    time.sleep(2)
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[1]/div[2]/div/button[1]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # ----------------------------------------------------------
    random_category_id = f"cat{random.randint(1000, 9999)}"

    # Locate the Category Id input field and enter the generated Category ID
    category_id_field = driver.find_element(By.ID, "categoryId")
    category_id_field.send_keys(random_category_id)

    print(f"Random Category ID entered: {random_category_id}")
    # --------------------------------------------------------------
    category_name = "Category " + str(random.randint(1, 1000))

    # Locate the category name input field and enter the generated name
    category_input = driver.find_element(By.ID, "category_name")
    category_input.send_keys(category_name)
    time.sleep(3)
    # ------------------------------------------------------------
    descriptions = [
        "This is a sample description.",
        "Random product description goes here.",
        "Description for testing purposes.",
        "Detailed information about the item.",
        "General item description text."
    ]
    random_description = random.choice(descriptions)

    # Locate the description field and enter the generated description
    description_field = driver.find_element(By.ID, "description")
    description_field.send_keys(random_description)
    time.sleep(3)
    # ------------------------------------------------------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#create_new_category_form > div.text-center.bg-body-secondary.py-3.rounded-bottom > button.btn.btn-primary.btn-sm")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # ------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[12]/div/div/div/div[4]/div/button")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # ------------------Filter-------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[1]/div[2]/div/button[3]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # ------------------------------------
    dropdown_element = driver.find_element(By.NAME, "isDistanceTherapy")

    # Initialize the Select class and choose a random option
    dropdown = Select(dropdown_element)
    dropdown.select_by_value(random.choice(["YES", "NO"]))
    time.sleep(3)
    # --------------------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/form/div/div/div[2]/button[2]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -----------------------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/form/div/div/div[2]/button[1]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -----------------------------------------

    category_links = driver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/table/tbody/tr[1]/td[2]")
    random.choice(category_links).click()
    time.sleep(3)
    # ------------------Edit button-------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[1]/div[2]/div/button[1]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # ---------------------------
    dropdown = Select(driver.find_element(By.ID, "Is_distance_therapy"))

    # Get all options except the currently selected one
    options = [option for option in dropdown.options if not option.is_selected()]

    # Select a random option from the unselected options
    random.choice(options).click()
    time.sleep(3)
    # --------------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[2]/form/div[2]/div[4]/div/div/button[2]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -----------------Ok----------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[7]/div/div/div/div[3]/div/button")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -----------Delete------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[4]/div[1]/div[2]/div/button[2]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -------------------------Confirmation msg--------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[10]/div/div/div/div[2]/div/button[1]")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)

    # ---------------------------------------------------------------------
    button = driver.find_element(By.XPATH,
                                 "/html/body/div[11]/div/div/div/div[3]/div/button")  # Replace with the actual button's selector
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    driver.quit()