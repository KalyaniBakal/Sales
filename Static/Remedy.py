
import mysql.connector
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import random
import string
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://185.199.53.169:5000/login")
time.sleep(2)
username_field = driver.find_element(By.NAME, "username")  # Replace with actual name attribute
password_field = driver.find_element(By.NAME, "password")  # Replace with actual name attribute

username_field.send_keys("9359146811")  # Replace with correct username or phone number
password_field.send_keys("Kalyani@1234")
password_field.send_keys(Keys.RETURN)

print(driver.current_url)
if "/dashboard" in driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")


driver.get("http://185.199.53.169:5000/getRemedy")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "i.bi.bi-sort-down").click()
time.sleep(2)
print("Sorted")
driver.find_element(By.ID, "new").click()
time.sleep(2)
def generate_unique_remedy_id():
    connection = mysql.connector.connect(
        host="185.199.53.169",
        user="lovenheal_user",
        password="lovenheal_user",
        database="lovenheal_server"
    )
    cursor = connection.cursor()

    while True:

        remedy_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return remedy_id

        query = "SELECT COUNT(*) FROM remedies WHERE remedy_id = %s"
        cursor.execute(query, (remedy_id,))
        result = cursor.fetchone()

        # If no records found with the generated ID, it’s unique
        if result[0] == 0:
            break

    # Close the connection
    cursor.close()
    connection.close()

    return remedy_id

time.sleep(2)
unique_remedy_id = generate_unique_remedy_id()
remedy_id_field = driver.find_element("id", "remedyId")
remedy_id_field.send_keys(unique_remedy_id)


file_input = driver.find_element(By.ID, "fileId")
file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
time.sleep(2)
driver.find_element(By.ID, "remedyName").send_keys("Chakra1")

dropdown = driver.find_element(By.ID, "remedyType")
dropdown.click()
time.sleep(1)
option = driver.find_element(By.CSS_SELECTOR, "option[value='AFFIRMATION']")
option.click()

filename_input = driver.find_element(By.ID, "fileName")
filename_input.send_keys("example_filename")

textarea = driver.find_element(By.ID, "remedyDescription")
textarea.send_keys("This is the remedy description.")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#alert_message_model > div > div > div.modal-body > div.row.mt-2 > div > button").click()
time.sleep(3)
print("remedy cereated successfully")

driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[2]/a").click()
time.sleep(2)

driver.find_element(By.ID,"edit").click()
time.sleep(2)
#
driver.find_element(By.CSS_SELECTOR, "i.bi.bi-pencil").click()
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
time.sleep(2)
driver.find_element(By.ID,"fileName").send_keys("opop")
time.sleep(1)
driver.execute_script("document.querySelector('button.btn.btn-primary').click();")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div[2]/div/button').click()
time.sleep(1)
print("File uploaded successfully")
driver.find_element(By.ID,"edit").click()
time.sleep(2)
remedy_name_input = driver.find_element(By.ID, "edit-remedy-name")
remedy_name_input.clear()
remedy_name_input.send_keys("New Remedy Name")

remedy_desc_textarea = driver.find_element(By.ID, "edit-remedy-desc")
remedy_desc_textarea.clear()
remedy_desc_textarea.send_keys("Updated description for relationships.")


driver.find_element(By.ID, "save").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div[7]/div/div/div[2]/div[2]/div/button").click()
time.sleep(2)
#driver.find_element(By.ID, "cancel").click()

driver.find_element(By.ID, "delete").click()
time.sleep(2)
driver.find_element(By.ID, "confirmDeleteButton").click()
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div[2]/div/button").click()
time.sleep(2)
driver.quit()