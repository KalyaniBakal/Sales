import logging
import datetime
import random
import string
import datetime
import time
from datetime import timedelta

from selenium.webdriver import Keys

import databseConnection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from FeedBack import generate_random_date
from Functions import random_name, generate_random_name, generate_present_date


def coupons(driver):
    driver.find_element(By.ID, "coupon_button").click()
    time.sleep(4)

    #--------Filters----------------------------------------------------------
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


    select_element = driver.find_element(By.ID, "name")
    dropdown = Select(select_element)
    all_options = dropdown.options[1:]
    random_option = random.choice(all_options)
    dropdown.select_by_visible_text(random_option.text)

    select_element = driver.find_element(By.ID, "status")
    dropdown = Select(select_element)
    all_options = dropdown.options[1:]
    random_option = random.choice(all_options)
    dropdown.select_by_visible_text(random_option.text)
    time.sleep(3)

    search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_button.click()
    print("Filter successfully")
    logging.info("Coupons Filter Successfully")
    time.sleep(3)

    reset_link = driver.find_element(By.XPATH, "//a[text()='Reset all']")
    reset_link.click()
    time.sleep(3)
    #------------------Create Coupons------------------------------------------------
    create_coupon_button = driver.find_element(By.XPATH, "//button[@data-bs-target='#create_coupon']")
    create_coupon_button.click()
    time.sleep(3)

    def coupons_mandatory_fields():
        driver.find_element(By.NAME, "coupon_name").send_keys(random_name)
        connection = databseConnection.conn()
        cursor = connection.cursor()

        while True:
            coupon_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # Generate random code
            query = "SELECT 1 FROM coupons WHERE code = %s"
            cursor.execute(query, (coupon_code,))
            result = cursor.fetchone()  # Check if the code exists
            if not result:  # If code doesn't exist, it's unique
                break
        search_input = driver.find_element(By.NAME, "coupon_code")
        search_input.send_keys(coupon_code)
        time.sleep(5)

        random_value = random.randint(1, 100)
        driver.find_element(By.NAME, "discount_value").send_keys(random_value)
        time.sleep(3)

    def coupons_non_mandatory_fields():
        random_value = random.randint(1, 100)
        total_usage_field = driver.find_element(By.NAME, "totalUsageCount")
        total_usage_field.send_keys(str(random_value))

        current_date = generate_present_date()
        days_to_add = random.randint(1, 365)
        end_date = current_date + datetime.timedelta(days=days_to_add)
        formatted_end_date = end_date.strftime("%d-%m-%Y")
        expiry_date_field = driver.find_element(By.NAME, "expiryDate")
        expiry_date_field.send_keys(formatted_end_date)
        expiry_date_field.send_keys(Keys.RETURN)


        offer_type_dropdown = driver.find_element(By.NAME,"offer_type")
        select = Select(offer_type_dropdown)
        options = select.options
        print("Available options:", [option.text for option in options])
        random_option = random.choice(options)
        select.select_by_visible_text(random_option.text)

        # public_radio = driver.find_element(By.ID, 'public')
        # personal_radio = driver.find_element(By.ID, 'personal')
        # selected_radio = random.choice([public_radio, personal_radio])
        # selected_radio.click()
        # time.sleep(3)


    def coupon_submit():
        try:
            # Locate the button using its class and click it
            create_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm")
            create_button.click()
            print("Button clicked successfully!")
            time.sleep(4)
            ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
            ok_button.click()
            print("OK button clicked.")

        except Exception as e:
            print(f"Error: {e}")
        logging.info("Coupons Created Successfully")
        time.sleep(3)

    coupons_mandatory_fields()
    coupons_non_mandatory_fields()
    coupon_submit()

    #------------------Edit-----------------------------------------------------------------------
    time.sleep(3)
    driver.find_element(By.XPATH, f"//tbody[@id='table_body']/tr[1]/td[2]/a").click()

    edit_button = driver.find_element(By.XPATH, "//button[text()='Edit']")
    edit_button.click()
    print("Edit button clicked.")
    time.sleep(3)

    coupon_name_input = driver.find_element(By.NAME, "coupon_name")
    random_coupon_name = generate_random_name()
    coupon_name_input.clear()
    coupon_name_input.send_keys(random_coupon_name)
    print("Random Coupon Name set to:", random_coupon_name)
    time.sleep(3)

    expiry_date_input = driver.find_element(By.ID, "expiryDate")
    expiry_date_value = expiry_date_input.get_attribute("value")
    print("Current Expiry Date:", expiry_date_value)
    current_date = datetime.strptime(expiry_date_value, "%d-%m-%Y")
    new_date = current_date + timedelta(days=3)
    formatted_new_date = new_date.strftime("%d-%m-%Y")
    expiry_date_input.clear()
    expiry_date_input.send_keys(formatted_new_date)

    print("New Expiry Date set to:", formatted_new_date)
    time.sleep(3)

    update_button = driver.find_element(By.XPATH, "//button[text()='Update']")
    update_button.click()
    print("Update button clicked.")
    time.sleep(3)

    ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
    ok_button.click()
    print("OK button clicked.")
    time.sleep(3)

    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
    delete_button.click()
    print("Delete button clicked.")
    time.sleep(3)

    yes_button = driver.find_element(By.ID, "yes_i_confirm")
    yes_button.click()
    print("Yes button clicked.")
    time.sleep(3)

    ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
    ok_button.click()
    print("OK button clicked.")
    time.sleep(3)

    # driver.execute_script("document.querySelector('i.bi.bi-chevron-left').click()")

    # -----------------Remove coupon-------------------------------------------------------------

    trash_icon = driver.find_element(By.CLASS_NAME, "bi-trash-fill")
    trash_icon.click()
    time.sleep(2)

    yes_button = driver.find_element(By.ID, "yes_i_confirm")
    yes_button.click()
    print("Yes button clicked.")
    time.sleep(2)

    ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
    ok_button.click()
    print("OK button clicked.")
    time.sleep(2)




