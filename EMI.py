import databseConnection
import random
import datetime
import time
from datetime import timedelta
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Functions import generate_random_date



def emi(driver):
    driver.get("http://185.199.53.169:5000/emis")
    time.sleep(3)

    #-----------------Sort-------------------------------
    for i in range(2):
        driver.find_element(By.ID, "sortButton").click()
        time.sleep(2)
        print("Sorted")

    #----------------Filter-------------------------------
    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "select customer_name from emis"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "customerName")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH, f"//div[@id='dropdown-content']//div[contains(text(), '{customer_name}')]").click()
    time.sleep(2)

    query = "SELECT SUBSTRING(booking_id, 1, 5) AS booking_id FROM emis;"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = str(result[0][0]).zfill(5)
    print(customer_name)
    search_input = driver.find_element(By.NAME, "bookingId")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH,
                        f"//div[@id='dropdown-booking-content']//div[contains(text(), '{customer_name}')]").click()
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
    end_date_input.send_keys(Keys.ESCAPE)

    radio_buttons = driver.find_elements(By.NAME, "showStatus")
    random_button = random.choice(radio_buttons)
    random_button.click()

    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()
    time.sleep(3)

    reset_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Reset all')]")
    reset_button.click()
    time.sleep(3)

    #-------------------------Add EMI-----------------------------------------

    driver.find_element(By.ID, "addNewEmi").click()
    time.sleep(2)

    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "select customer_name from emis"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "search_name")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH, f"//div[@id='dropdown_result']//span[contains(text(), '{customer_name}')]").click()

    time.sleep(2)

    query = "SELECT b.remaining_amount FROM emis e LEFT JOIN bookings b ON b.booking_for = e.customer_name;"
    cursor.execute(query)
    result = cursor.fetchall()
    remaining_amount = result[0][0]
    if remaining_amount > 1:
        paid_amount = random.randint(1, remaining_amount - 1)
    else:
        paid_amount = 0

    print(f"Generated random paid amount: {paid_amount}")
    print(f"Remaining amount: {remaining_amount}")

    if paid_amount > 0:
        search_input = driver.find_element(By.NAME, "paidAmount")
        search_input.send_keys(str(paid_amount))
    else:
        print("Error: Remaining amount is too low to generate a valid paid amount.")

    time.sleep(3)
    query = "SELECT e.next_payment_date FROM  emis e LEFT JOIN bookings b ON b.booking_for = e.customer_name;"
    cursor.execute(query)
    result = cursor.fetchall()
    next_payment_date = result[0][0]
    print(next_payment_date)
    updated_date = next_payment_date + timedelta(days=2)
    formatted_date = updated_date.strftime("%d-%m-%Y")
    search_input = driver.find_element(By.ID, "nextPaymentDate")
    search_input.send_keys(formatted_date)
    search_input.send_keys(Keys.ESCAPE)
    time.sleep(3)

    driver.find_element(By.ID, "fileId").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-sm.px-4").click()

    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[10]/div/div/div/div[4]/div/button").click()
    time.sleep(2)

    #-----------------------Edit----------------------------------------------------
    driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[3]/a").click()
    time.sleep(2)
    try:
        # Attempt to locate and click the image icon
        driver.find_element(By.CSS_SELECTOR, "i.bi.bi-image-alt").click()
        print("Image icon clicked.")
        time.sleep(4)
        driver.find_element(By.CLASS_NAME, "btn-close").click()
    except NoSuchElementException:
        print("Image icon not found. Moving to the next button.")
        # driver.find_element(By.XPATH, "//button[contains(text(), 'Add EMI')]").click()

    finally:

        driver.find_element(By.XPATH, "//button[contains(text(), 'Add EMI')]").click()
        time.sleep(2)

    query = "SELECT b.remaining_amount FROM emis e LEFT JOIN bookings b ON b.booking_for = e.customer_name;"
    cursor.execute(query)
    result = cursor.fetchall()
    remaining_amount = result[0][0]
    if remaining_amount > 1:
        paid_amount = random.randint(1, remaining_amount - 1)
    else:
        paid_amount = 0

    print(f"Generated random paid amount: {paid_amount}")
    print(f"Remaining amount: {remaining_amount}")

    if paid_amount > 0:
        search_input = driver.find_element(By.NAME, "paidAmount")
        search_input.send_keys(str(paid_amount))
    else:
        print("Error: Remaining amount is too low to generate a valid paid amount.")

    time.sleep(3)
    query = "SELECT e.next_payment_date FROM  emis e LEFT JOIN bookings b ON b.booking_for = e.customer_name;"
    cursor.execute(query)
    result = cursor.fetchall()
    next_payment_date = result[0][0]
    print(next_payment_date)
    updated_date = next_payment_date + timedelta(days=2)
    formatted_date = updated_date.strftime("%d-%m-%Y")
    search_input = driver.find_element(By.ID, "nextPaymentDate")
    search_input.send_keys(formatted_date)
    search_input.send_keys(Keys.ESCAPE)
    time.sleep(3)

    driver.find_element(By.ID, "fileId").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")

    button = driver.find_element(By.XPATH, "//button[text()='Add']")
    button.click()

    time.sleep(4)

    driver.find_element(By.ID, "global_Success_Message_Btn").click()
    time.sleep(4)

    #------------------------View all Emi-------------
    driver.find_element(By.XPATH, "//span[contains(text(), '< View all emi')]").click()
    time.sleep(2)

    #-----------------------Delete---------------------
    driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[3]/a").click()
    time.sleep(3)
    driver.find_element(By.ID, "deleteEmi").click()
    time.sleep(2)
    driver.find_element(By.ID, "confirm_delete_emi").click()
    time.sleep(10)
    driver.execute_script("""document.querySelector("#global_Success_Message_Model_With_Id > div > div > div > div.row.mt-2.py-2.mb-2 > div > button").click();""")
    time.sleep(2)
    print("Deleted Successfully")






