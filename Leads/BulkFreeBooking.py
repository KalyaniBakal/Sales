import datetime
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


def generate_random_date(start_date, end_date):
    days_between_dates = (end_date - start_date).days
    random_days = random.randint(0, days_between_dates)
    return start_date + datetime.timedelta(days=random_days)

today = datetime.date.today()
past_date = generate_random_date(today - datetime.timedelta(days=365), today - datetime.timedelta(days=1))  # Past
present_date = today  # Present
future_date = generate_random_date(today + datetime.timedelta(days=1), today + datetime.timedelta(days=365))  # Future

# Choose which date to use
selected_date = past_date  # Change to `present_date` or `future_date` as needed
formatted_date = selected_date.strftime("%d-%m-%Y")

def generate_random_4_digit_time():
    hour = random.randint(0, 11)  # Random hour between 00 and 11 (12-hour format)
    minute = random.randint(0, 59)  # Random minute between 00 and 59
    return f"{hour:02d}{minute:02d}"

def bulk_free_booking(driver):
    driver.get("http://185.199.53.169:5000/marketing-leads")
    time.sleep(3)

    rows_to_click = [1, 2, 3]
    for row in rows_to_click:
        checkbox_element = driver.find_element(By.XPATH, f"(//tbody/tr[{row}]//td/input[@type='checkbox'])")
        checkbox_element.click()
    time.sleep(3)

    bulk_booking_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#bulk_free_booking_model']"))
    )

    # Click the button
    bulk_booking_button.click()

    time.sleep(4)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "select_date")))
    driver.execute_script(f"document.getElementById('select_date').value = '{formatted_date}';")
    driver.find_element(By.ID, "select_date").get_attribute("value")
    time.sleep(4)

    start_time_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "start_time_input"))
    )
    random_start_time = generate_random_4_digit_time()
    start_time_input.clear()
    start_time_input.send_keys(random_start_time)
    time.sleep(4)
    driver.execute_script("document.getElementById('start_time_pm').checked = true;")
    # driver.execute_script("document.getElementById('start_time_am').checked = true;")

    end_time_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "end_time_input"))
    )
    random_end_time = generate_random_4_digit_time()
    end_time_input.clear()
    end_time_input.send_keys(random_end_time)
    driver.execute_script("document.getElementById('end_time_pm').checked = true;")
    # driver.execute_script("document.getElementById('end_time_am').checked = true;")
    time.sleep(4)

    create_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit_bulk_free_bookings"))
    )
    create_button.click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div[21]/div/div/div/div[3]/div/button").click()
    time.sleep(3)