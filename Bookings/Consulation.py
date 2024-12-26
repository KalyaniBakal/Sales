from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import random
import time
from datetime import datetime, timedelta
driver = webdriver.Chrome()

driver.get("http://185.199.53.169:5000/login")
driver.maximize_window()

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("8788757703")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Admin@12345@")

password_input.send_keys(Keys.RETURN)
time.sleep(2)
print(driver.current_url)
if "/dashboard" in driver.current_url:
    print("Login Successful - Redirected to Dashboard")
else:
    print("Login Failed - Redirected to Unexpected URL")
time.sleep(2)

driver.get("http://185.199.53.169:5000/bookings")
time.sleep(3)

driver.find_element(By.XPATH, "(//tbody/tr)[1]/td[2]/a").click()

button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[2]/div/button[1]")
driver.execute_script("arguments[0].click();", button)
time.sleep(3)

def cons_mandatory_field():
 random_notes = [
        "This is the first random note.",
        "Important lead information.",
        "Follow up in a week.",
        "Need to review the details.",
        "Lead requires immediate attention."
    ]

 note = random.choice(random_notes)
 notes_field = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[2]/form/div[8]/div/textarea")
 notes_field.clear()
 notes_field.send_keys(note)
 time.sleep(2)

def cons_non_mandatory_fields():
 random_phone = f"+919{''.join([str(random.randint(0, 9)) for _ in range(9)])}"
 phone_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div[2]/form/div[2]/div[2]/input")))
 phone_input.clear()
 phone_input.send_keys(random_phone)
 time.sleep(3)

 dob = (datetime.now() - timedelta(days=random.randint(7300, 18250))).strftime("%d-%m-%Y")
 dob_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "consultation_customer_dob")))
 existing_dob = dob_input.get_attribute("value")
 if existing_dob:
  print(f"Existing DOB found: {existing_dob}. Replacing it with new DOB: {dob}")
 dob_input.clear()
 dob_input.send_keys(dob)

 body_element = driver.find_element(By.TAG_NAME, "body")
 ActionChains(driver).move_to_element(body_element).click().perform()
 time.sleep(3)

 duration=driver.find_element(By.NAME,"call_duration")
 call=random.randint(1,90)
 duration.send_keys(call)
 time.sleep(2)
#--------Title-----------------
 consultation_titles = [
          "Health Consultation with Specialist",
          "Mental Wellness Session",
          "Nutrition and Diet Advice",
          "Follow-up Consultation",
          "General Check-up",
          "Therapy Session",
          "Lifestyle Coaching Session",
          "Chronic Condition Management",
          "Personalized Health Assessment",
          "Stress Management Consultation"
      ]
 random_title = random.choice(consultation_titles)
 title_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[11]/div/div/div[2]/form/div[4]/div/input')))
 title_input.send_keys(random_title)
 time.sleep(3)

 WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-check-input"))
 )

 checkboxes = driver.find_elements(By.CSS_SELECTOR, ".form-check-input")

 if len(checkboxes) >= 3:
     random.shuffle(checkboxes)
     selected_checkboxes = checkboxes[:3]

     for checkbox in selected_checkboxes:
         if checkbox.is_displayed() and checkbox.is_enabled():
             checkbox.click()
             print(f"Selected checkbox with value: {checkbox.get_attribute('value')}")
         else:
             print("Checkbox not interactable.")
 else:
     print(f"Not enough checkboxes to select 3. Found {len(checkboxes)} checkboxes.")

 dropdown = Select(driver.find_element(By.ID, "remedy_given"))
 options = dropdown.options
 random.choice(options).click()
 time.sleep(3)


def submit():
 save_button = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div[3]/div/div/button[2]")
 save_button.click()
 time.sleep(2)
 button = driver.find_element(By.XPATH,
                              "/html/body/div[14]/div/div/div/div[3]/div/button")
 driver.execute_script("arguments[0].click();", button)
 time.sleep(3)


cons_mandatory_field()
cons_non_mandatory_fields()
submit()

driver.quit()
