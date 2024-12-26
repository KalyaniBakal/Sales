import string
import time

from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime, timedelta
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://185.199.53.169:5000/login")

username_field = driver.find_element(By.NAME, "username")  # Replace with actual name attribute
password_field = driver.find_element(By.NAME, "password")  # Replace with actual name attribute

username_field.send_keys("9359146811")  # Replace with correct username or phone number
password_field.send_keys("Kalyani@12345")

password_field.send_keys(Keys.RETURN)
#time.sleep(3)
print(driver.current_url)
if "/dashboard" in driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")

driver.get("http://185.199.53.169:5000/marketing-leads")
lead = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[3]/table/tbody/tr[1]/td[2]/a")))  # Replace 'New Lead' with actual lead name
driver.execute_script("arguments[0].click();", lead)
def generate_random_filename():
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=5))  # Random 5-character string
   # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Timestamp for uniqueness
    return random_part

camera_img = driver.find_element(By.XPATH, "//img[contains(@src, 'camera-dim.svg')]")
camera_img.click()
time.sleep(2)

file_path="C:/Users/bakal/OneDrive/Desktop/boy.jpeg"
upload_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "upload_multiple_cutomer_photo-image-view"))
        )
for i in range(3):
    try:

        file_input = driver.find_element(By.ID, "input-customer-file")
        driver.execute_script("arguments[0].value = '';", file_input)

        file_input.send_keys(file_path)  # Update path if needed
        time.sleep(2)

        upload_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div/form/label/div[4]/button"))
        )
        upload_button.click()
        time.sleep(2)

        # Wait for the success message button to be clickable
        wait = WebDriverWait(driver, 10)
        ok_button = wait.until(EC.element_to_be_clickable((By.ID, "global_Success_Message_Btn")))

        # Click the success button to acknowledge the upload
        ok_button.click()
        time.sleep(3)
        if i < 2:
            camera_lead = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "extra_camera_lead"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", camera_lead)
            camera_lead.click()

        print(f"Iteration {i + 1}: File uploaded successfully.")
    except Exception as e:
        print(f"Iteration {i + 1}: Failed with error: {e}")

time.sleep(3)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "fetchfileId-container"))
)

# Get all photo elements
photo_elements = driver.find_elements(By.CLASS_NAME, "lead_extra_photo")

if photo_elements:
    # Choose a random photo
    random_photo = random.choice(photo_elements)

    # Scroll the photo into view
    driver.execute_script("arguments[0].scrollIntoView(true);", random_photo)

    # Click on the chosen photo
    random_photo.click()

    print("Photo clicked successfully.")
else:
    print("No photos found to click.")
time.sleep(4)

chevron_span = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".chevron.right-chevron"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", chevron_span)
chevron_span.click()
time.sleep(4)
print("Chevron icon clicked successfully!")

wait = WebDriverWait(driver, 10)
delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[5]/div/div/div[2]/div/img")))
delete_button.click()
time.sleep(4)

ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
ok_button.click()
print("Deleted successfully")

def generate_random_filename():
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=5))  # Random 5-character string
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Timestamp for uniqueness
    return f"file_{random_part}_{timestamp}"
# edit_button = driver.find_element(By.ID, "editLeadBtn")
# edit_button.click()
# time.sleep(2)
# camera_div = driver.find_element(By.ID, "upload_photo")
# camera_div.click()
# time.sleep(2)
# file_input = driver.find_element(By.ID, 'input-file')
# file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/boy.jpeg")
# time.sleep(2)
# driver.find_element(By.ID, "filename").send_keys(generate_random_filename())
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[7]/div/div/form/label/div[4]/button").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div[26]/div/div/div/div[3]/div/button").click()
# time.sleep(1)
# #-----------------------Free Booking Tab----------------------------------------------------------
# driver.find_element(By.ID,"free-booking-tab").click()
# time.sleep(3)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
#
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[1]/div[2]/button[1]").click()
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[2]/div[1]/div[1]/div/input[2]').clear()
# driver.find_element(By.XPATH, '/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[2]/div[1]/div[1]/div/input[2]').send_keys('John Doe')
#
# time.sleep(2)
# wish1 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[2]/div[4]/div[1]/div/input[2]")
# wish1.send_keys("Fever")
#
# driver.find_element(By.NAME, 'allottedInstructions').clear()
# driver.find_element(By.NAME, 'allottedInstructions').send_keys('Follow these specific instructions.')
#
# driver.execute_script("window.scrollTo(0, 300);")
# time.sleep(3)
#
# driver.find_element(By.CSS_SELECTOR, 'button.free-booking-save-button-1').click()
# time.sleep(3)
#
# print("Edited free booking successfully")
#
# driver.find_element(By.XPATH,"/html/body/div[26]/div/div/div/div[3]/div/button").click()
# time.sleep(3)
# #-----------------------Paid Booking Tab----------------------------------------------------------
# driver.find_element(By.ID,"paid-booking-tab").click()
# time.sleep(3)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
#
#
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[1]/div[2]/button[1]").click()
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[2]/div[3]/div[2]/div/input[2]').clear()
# driver.find_element(By.XPATH, '/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[2]/div[3]/div[2]/div/input[2]').send_keys('John Doe')
#
#
# random_phone_number = "+91" + str(random.randint(6000000000, 9999999999))
# gifteePhoneNo = driver.find_element(By.NAME, 'gifteePhoneNo')
# gifteePhoneNo.clear()
# gifteePhoneNo.send_keys(random_phone_number)
#
# time.sleep(2)
# wish1 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[2]/div[7]/div[1]/div/input[2]")
# wish1.send_keys("Fever")
#
# driver.execute_script("window.scrollTo(0, 300);")
# time.sleep(3)
#
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[1]/div[2]/button[3]").click()
# time.sleep(3)
#
# print("Edited paid booking successfully")

# driver.find_element(By.XPATH,"/html/body/div[26]/div/div/div/div[3]/div/button").click()
# time.sleep(3)
# driver.find_element(By.ID, "issues-tab").click()
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
# add_issue_button = driver.find_element(By.XPATH, '//button[@class="Consultation-history-btn btn btn-primary" and @data-bs-toggle="modal" and @data-bs-target="#Open-Issue"]')
# add_issue_button.click()
# time.sleep(2)
# driver.find_element(By.ID, "raise-1").click()
# time.sleep(2)
# driver.find_element(By.ID, "comments").send_keys("I am facing this issue")
# Select(driver.find_element(By.ID, "category")).select_by_visible_text("FEEDBACK")
# Select(driver.find_element(By.ID, "priority")).select_by_value("2")
# time.sleep(3)
# driver.find_element(By.XPATH, '//*[@id="file"]').send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, "#Open-Other-Issue > div > div > form > div:nth-child(2) > button.btn.btn-primary").click()
# time.sleep(4)
# button = driver.find_element(By.CSS_SELECTOR, "#global_Success_Message_Model_With_Id > div > div > div > div.row.mt-2.py-2.mb-2 > div > button")
# button.click()
# print("Issue created")
# time.sleep(3)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
# edit_button = driver.find_element(By.CSS_SELECTOR, 'button.issue-edit-button')
# edit_button.click()
# comments = driver.find_element(By.NAME, 'comments')
# comments.send_keys("Adding a random comment for testing purposes.")
# priority = driver.find_element(By.NAME, 'priority')
# select = Select(priority)
# select.select_by_value('2')
# driver.find_element(By.ID,"files").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
# time.sleep(3)
# driver.execute_script("window.scrollTo(0, 300);")
# time.sleep(3)
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div[9]/div/div[2]/div/div/div/form/div[1]/div[2]/button[3]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[26]/div/div/div/div[3]/div/button").click()
# time.sleep(2)

# driver.find_element(By.ID,"feedback-tab").click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
#
# edit_button = driver.find_element(By.CLASS_NAME, 'feedback-edit-button')
# edit_button.click()
#
#
# # ---------------------------------------------
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
#
# # ------------------------------------------------
# driver.find_element(By.XPATH, '/html/body/div[4]/div/div[10]/div/div[2]/div[1]/div/div/form/div[2]/div[3]/div[1]/div/select').click()
#
# # Locate the specific option by its value and click it
# option = driver.find_element(By.XPATH, "//select[@id='feedback-type']/option[@value='IMAGE']")
# option.click()
#
#
# feedback_textarea = driver.find_element(By.NAME, 'feedback')
# feedback_textarea.clear()
# feedback_textarea.send_keys("Please review my feedback and suggest improvements.")
# driver.find_element(By.ID, "feedback-files-1").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
# time.sleep(3)
# driver.execute_script("window.scrollTo(0, 300);")
# time.sleep(3)
# driver.find_element(By.XPATH,
#                     "/html/body/div[4]/div/div[10]/div/div[2]/div[1]/div/div/form/div[1]/div[2]/button[3]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div[26]/div/div/div/div[3]/div/button").click()
# time.sleep(2)
driver.quit()


