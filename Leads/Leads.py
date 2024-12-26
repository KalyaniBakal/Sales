import string
import time
from .BulkFreeBooking import bulk_free_booking
from .NewLead import new_lead
from .QR_Consnet import QR
import driver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime, timedelta
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import databseConnection

def generate_random_date(start, end):
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))

# Define the date range
start_date, end_date = datetime.date(2024, 11, 1), datetime.date(2024, 12, 31)
random_start = generate_random_date(start_date, end_date)
random_end = generate_random_date(random_start, end_date)

# Format dates
formatted_start = random_start.strftime("%d-%m-%Y")
formatted_end = random_end.strftime("%d-%m-%Y")

def leads(driver):

    driver.get("http://185.199.53.169:5000/marketing-leads")
    time.sleep(3)

    for i in range(1, 3):  # Loop from 1 to 2
        button = driver.find_element(By.ID, "sort_button")  # Locate the button by its ID
        button.click()  # Click the button
        time.sleep(3)

   # QR(driver)

    #bulk_free_booking(driver)

    filter_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Filter')]")
    filter_button.click()
    time.sleep(2)

    connection = databseConnection.conn()
    cursor = connection.cursor()
    queries = ["select name from marketing_leads",
    "SELECT SUBSTRING(mobile_no, 4) AS mobile_no FROM marketing_leads ORDER BY mobile_no DESC"]
    random_query = random.choice(queries)
    cursor.execute(random_query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "search_lead_name")
    search_input.send_keys(customer_name)
    time.sleep(5)


    start_date_input = driver.find_element(By.ID, "start-date")
    end_date_input = driver.find_element(By.ID, "end-date")

    # Ensure fields are clickable using ActionChains
    actions = ActionChains(driver)

    # Click and input start date
    actions.move_to_element(start_date_input).click().perform()
    time.sleep(1)  # Allow time for focus
    start_date_input.clear()
    start_date_input.send_keys(formatted_start)
    time.sleep(1)  # Allow time for processing

    # Click and input end date
    actions.move_to_element(end_date_input).click().perform()
    time.sleep(1)  # Allow time for focus
    end_date_input.clear()
    end_date_input.send_keys(formatted_end)
    time.sleep(4)

    select = Select(driver.find_element(By.NAME, 'leadSource'))
    options = select.options
    random_option = random.choice(options[1:]) if options[0].text == 'Select' else random.choice(options)
    select.select_by_visible_text(random_option.text)
    time.sleep(2)

    select = Select(driver.find_element(By.NAME, 'leadStatus'))
    options = select.options
    random_option = random.choice(options[1:]) if options[0].text == 'Select' else random.choice(options)
    select.select_by_visible_text(random_option.text)
    time.sleep(2)
    # ---------------------------Search button------------------------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.btn-outline-primary")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    # -------------------------Reset All button----------------------------------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.bg-white.text-primary")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    # -------------------------------New Lead button-----------------------------------------
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#main-container > div.col-12.bg-white.rounded.d-flex.p-2 > div.col-sm-4.d-flex.justify-content-between.align-items-center.pe-2 > div:nth-child(2) > button:nth-child(1)")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)

    new_lead(driver)
    # ------------------------Wait for the lead to be visible, then click on it------------------------
    lead = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[4]/div[3]/table/tbody/tr[1]/td[2]/a")))  # Replace 'New Lead' with actual lead name
    driver.execute_script("arguments[0].click();", lead)
    # -------------------------------click on edit button-----------------
    edit_button = driver.find_element(By.ID, "editLeadBtn")
    edit_button.click()
    time.sleep(2)
    # --------------Enter email id-----------------------
    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys("sumeet1234@gmail.com")
    # ---------------Add DOB----------------------------------
    dob_field = driver.find_element(By.NAME, "dob")  # Replace "dob" with the actual name attribute of the DOB field
    dob_field.clear()
    dob_field.send_keys("01-01-2000")

    # ------------------------Change Lead source, select from the dropdown------------------------
    lead_source_dropdown = Select(driver.find_element(By.NAME, "leadSource"))

    lead_source_dropdown.select_by_visible_text("FACEBOOK")
    # -------------------------Change status------------------------------
    new = driver.find_element(By.ID, "new")
    new.click()

    # --------------------------Select gender-------------------------------------
    driver.find_element(By.ID, "femaleRadio").click()  # Uncomment for Female
    time.sleep(3)

    # ----------------------Click on update button----------------------------------
    update_button = driver.find_element(By.CSS_SELECTOR, '#saveEdit')
    update_button.click()
    time.sleep(3)
    # ---------------------Click on Ok button on the popup-----------------------------
    ok_button = driver.find_element(By.CSS_SELECTOR,
                                    "#global_Success_Message_Model > div > div > div > div.row.mt-2.py-2.mb-2 > div > button")
    driver.execute_script("arguments[0].click();", ok_button)
    driver.execute_script("document.querySelector('button[data-bs-dismiss=\"modal\"]').click()")
    print("Edit successful")
    time.sleep(4)

    # ---------------Create Call---------------------------
    driver.execute_script(
        "document.querySelector('button.btn.btn-sm.btn-outline-primary.border-secondary-subtle').click();")
    time.sleep(3)
    call_duration_field = driver.find_element(By.ID, "callDuration")
    call_duration_field.send_keys("10")

    call_status_answered = driver.find_element(By.ID, "answered")
    call_status_unanswered = driver.find_element(By.ID, "unanswered")

    call_status_answered.click()

    notes_field = driver.find_element(By.NAME, "Notes")
    notes_field.send_keys("Customer was interested in the product.")
    time.sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm.px-3")
    save_button.click()
    print("Call created")
    driver.execute_script(
        """document.querySelector("button.btn.btn-outline-primary.btn-sm.px-3[data-bs-dismiss='modal']").click();""")
    time.sleep(2)
    # -----------------------------------Create Free Booking --------------------------
    driver.execute_script(
        """document.querySelector("button.btn.btn-sm.btn-outline-primary.border-secondary-subtle[data-bs-target='#BookFreeHealing']").click();""")
    time.sleep(2)

    Starttime_input = driver.find_element(By.ID, "Start_timeInput")
    Starttime_input.send_keys("12:30")
    driver.execute_script("document.getElementById('start_time_pm').checked = true;")

    Endtime_input = driver.find_element(By.ID, "End_timeInput")
    Endtime_input.send_keys("01:30")
    driver.execute_script("document.getElementById('end_time_pm').checked = true;")

    address_input = driver.find_element(By.ID, "AddressLine1")
    address_input.send_keys("123 Main St")

    wish = driver.find_element(By.ID, "Wish")
    wish.send_keys("Headache")

    allottedInstructions = driver.find_element(By.ID, "allottedInstructions")
    allottedInstructions.send_keys("Old Customer")
    time.sleep(4)
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Save"]')
    submit_button.click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[26]/div/div/div/div[3]/div/button").click()
    time.sleep(2)
    print("Create Free Booking")
    time.sleep(3)
    # -----------------------Free Booking Tab----------------------------------------------------------
    driver.find_element(By.ID, "free-booking-tab").click()
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    driver.find_element(By.XPATH,
                        "/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[1]/div[2]/button[1]").click()
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element(By.XPATH,
                        '/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[2]/div[1]/div[1]/div/input[2]').clear()
    driver.find_element(By.XPATH,
                        '/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[2]/div[1]/div[1]/div/input[2]').send_keys(
        'John Doe')

    time.sleep(2)
    wish1 = driver.find_element(By.XPATH,
                                "/html/body/div[4]/div/div[5]/div/div[2]/div/div/form/div[2]/div[4]/div[1]/div/input[2]")
    wish1.send_keys("Fever")

    driver.find_element(By.NAME, 'allottedInstructions').clear()
    driver.find_element(By.NAME, 'allottedInstructions').send_keys('Follow these specific instructions.')

    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, 'button.free-booking-save-button-1').click()
    time.sleep(3)

    print("Edited free booking successfully")

    driver.find_element(By.XPATH, "/html/body/div[26]/div/div/div/div[3]/div/button").click()
    time.sleep(3)
    driver.execute_script(
        "document.querySelector('button[data-bs-toggle=\"modal\"][data-bs-target=\"#paid_booking\"]').click();")
    time.sleep(1)
    address_input = driver.find_element(By.ID, "P_AddressLine1")
    address_input.send_keys("123 Main St")

    wish = driver.find_element(By.ID, "P_Wish")
    wish.send_keys("Headache")

    select_element = driver.find_element(By.ID, "P_Offerings")
    ("1 Day Healing")

    def generate_random_start_date():
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2024, 12, 31)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        random_start_date = start_date + timedelta(days=random_days)
        return random_start_date

    def generate_random_end_date(start_date):
        random_end_days = random.randint(1, 30)
        random_end_date = start_date + timedelta(days=random_end_days)
        return random_end_date

    start_date = generate_random_start_date()

    end_date = generate_random_end_date(start_date)

    start_date_input = driver.find_element(By.ID, 'P_StartDate')
    start_date_input.send_keys(start_date.strftime('%d-%m-%Y'))

    end_date_input = driver.find_element(By.ID, 'P_EndDate')
    end_date_input.send_keys(end_date.strftime('%d-%m-%Y'))

    Starttime_input = driver.find_element(By.ID, "P_Start_timeInput")
    Starttime_input.send_keys("12:30")
    driver.execute_script("document.getElementById('start_time_pm1').checked = true;")

    Endtime_input = driver.find_element(By.ID, "P_End_timeInput")
    Endtime_input.send_keys("01:30")
    driver.execute_script("document.getElementById('end_time_pm1').checked = true;")

    duration_input = driver.find_element(By.ID, "P_duration")
    duration_input.send_keys("30")

    # emi_radio_button = driver.find_element(By.ID, "WithEMI")
    # emi_radio_button.click()

    total_amount_input = driver.find_element(By.ID, "totalAmount")
    total_amount_input.send_keys("1000")

    # paid_amount_input = driver.find_element(By.ID, "paidAmount")
    # paid_amount_input.send_keys("500")

    file_input = driver.find_element(By.ID, "upload_payment_image")
    file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")

    instructions_textarea = driver.find_element(By.ID, "P_Allotted_Instructions")
    instructions_textarea.clear()  # Clear any existing text
    instructions_textarea.send_keys("Please follow the instructions carefully.")
    time.sleep(4)
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-sm.btn-primary.px-2")
    submit_button.click()
    time.sleep(3)
    print("Click on submitted button")
    driver.find_element(By.XPATH, "/html/body/div[27]/div/div/div/div[4]/div/button").click()
    print("Click on Ok button,Created paid booking")
    time.sleep(4)

    # ---------------------------Paid Booking Tab-----------------------------------------------------------------------

    driver.find_element(By.ID, "paid-booking-tab").click()
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[1]/div[2]/button[1]").click()
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element(By.XPATH,
                        '/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[2]/div[3]/div[2]/div/input[2]').clear()
    driver.find_element(By.XPATH,
                        '/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[2]/div[3]/div[2]/div/input[2]').send_keys(
        'John Doe')

    random_phone_number = "+91" + str(random.randint(6000000000, 9999999999))
    gifteePhoneNo = driver.find_element(By.NAME, 'gifteePhoneNo')
    gifteePhoneNo.clear()
    gifteePhoneNo.send_keys(random_phone_number)

    time.sleep(2)
    wish1 = driver.find_element(By.XPATH,
                                "/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[2]/div[7]/div[1]/div/input[2]")
    wish1.send_keys("Fever")

    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(3)

    driver.find_element(By.XPATH,
                        "/html/body/div[4]/div/div[6]/div/div[2]/div/div/form/div[1]/div[2]/button[3]").click()
    time.sleep(3)

    print("Edited paid booking successfully")

    driver.find_element(By.XPATH, "/html/body/div[26]/div/div/div/div[3]/div/button").click()
    time.sleep(3)
    # -------------------------Consent-------------------------
    consent_tab = driver.find_element(By.ID, "consent-tab")
    driver.execute_script("arguments[0].click();", consent_tab)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # -----------------------------------consultation-tab----------------------------------------------------------------------------
    consultation_tab = driver.find_element(By.ID, "consultation-tab")
    driver.execute_script("arguments[0].click();", consultation_tab)
    time.sleep(3)
    add_consultation_btn = driver.find_element(By.ID, "addConsultationBtn")
    driver.execute_script("arguments[0].click();", add_consultation_btn)
    time.sleep(3)
    # ---------------------------------------------------
    random_phone = f"9{''.join([str(random.randint(0, 9)) for _ in range(9)])}"

    # Input the random phone number
    phone_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "alternate_phone_no"))
    )
    phone_input.clear()
    phone_input.send_keys(random_phone)
    time.sleep(3)
    # ------------------------------------------------------
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

    # Select a random title from the list
    random_title = random.choice(consultation_titles)

    # Wait for the title input to be available
    title_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'title'))
    )

    # Enter the random consultation-related title into the input field
    title_input.send_keys(random_title)
    time.sleep(3)
    # ----------------------------------------------------------
    chakra_checkboxes = [
        "crownCheckbox",
        "thirdeyeCheckbox",
        "throatcheckbox",
        "heartcheckbox",
        "solarplexuscheckbox",
        "sacralcheckbox",
        "rootcheckbox"
    ]

    # Select a random chakra point from the list
    random_chakra = random.choice(chakra_checkboxes)

    # Find the checkbox by ID and click it using JavaScript
    chakra_checkbox = driver.find_element(By.ID, random_chakra)
    driver.execute_script("arguments[0].click();", chakra_checkbox)
    time.sleep(5)
    # -------------------------------------------------------------
    random_notes = [
        "This is the first random note.",
        "Important lead information.",
        "Follow up in a week.",
        "Need to review the details.",
        "Lead requires immediate attention."
    ]

    # Choose a random feedback message
    notes_text = random.choice(random_notes)

    # Locate the feedback textarea
    notes_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/form/div[1]/div[9]/div/div/textarea"))
    )

    # Use JavaScript to set the value directly without clearing the placeholder
    driver.execute_script("arguments[0].value = arguments[1];", notes_field, notes_text)
    time.sleep(3)
    # -----------------------
    button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/form/div[2]/button[2]")
    driver.execute_script("arguments[0].click();",
                          button)  # filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.bg-white.text-primary

    time.sleep(5)
    # -----------------------------------
    button = driver.find_element(By.XPATH, "/html/body/div[27]/div/div/div/div[4]/div/button")
    driver.execute_script("arguments[0].click();",
                          button)  # filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.bg-white.text-primary
    time.sleep(5)
    # ------------------------------------Medical History Tab---------------------------------------------------------------------------------
    medical_history_tab = driver.find_element(By.ID, "medical-history-tab")
    medical_history_tab.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")
    driver.execute_script("arguments[0].click();",
                          driver.find_element(By.XPATH, "//button[@data-bs-target='#New-Medical-History']"))
    time.sleep(2)
    file_input = driver.find_element(By.ID, "uploadDocument")
    file_input.send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
    docdetails = driver.find_element(By.ID, "doctorDetails")
    docdetails.send_keys("Mohan Sharma")
    hospital = driver.find_element(By.ID, "hospitalName")
    hospital.send_keys("Main Hospital")
    random_date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%d-%m-%Y")
    date_input = driver.find_element(By.ID, 'diagnosisDate')
    date_input.send_keys(random_date)
    issues = driver.find_element(By.ID, "medicalIssues")
    issues.send_keys("BP")
    time.sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary.btn-sm')
    save_button.click()

    time.sleep(3)
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#global_Success_Message_Model_With_Id > div > div > div > div.row.mt-2.py-2.mb-2 > div > button")
    button.click()

    time.sleep(3)
    print("Created medical history")
    # ---------------------------edit Medical History-----------------
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)
    # driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[12]/div/div[2]/div[1]/div/div[1]/div[2]/button[1]").click()
    # time.sleep(2)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)
    # medical_issues = driver.find_element(By.CSS_SELECTOR, 'input[name="medical_issues"].editable-field')
    # medical_issues.clear()
    # medical_issues.send_keys("New Value")
    # doctor = driver.find_element(By.CSS_SELECTOR, 'input[name="doctor"].editable-field')
    # doctor.clear()
    # doctor.send_keys("Updated Value")
    # hospital_name = driver.find_element(By.CSS_SELECTOR, 'input[name="hospital_name"].editable-field')
    # hospital_name.clear()
    # hospital_name.send_keys("New Hospital Name")
    # date = driver.find_element(By.CSS_SELECTOR, 'input#diagnosis_date.editable-field.hasDatepicker')
    # date.clear()
    # date.send_keys("08-11-2024")
    # time.sleep(3)
    # save_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.save-button[data-target="#Medical-History-1"]')
    # save_button.click()
    # time.sleep(4)
    # ---------------------Issue Created---------------------------------------------------------------------
    driver.find_element(By.ID, "issues-tab").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    add_issue_button = driver.find_element(By.XPATH,
                                           '//button[@class="Consultation-history-btn btn btn-primary" and @data-bs-toggle="modal" and @data-bs-target="#Open-Issue"]')
    add_issue_button.click()
    time.sleep(2)
    driver.find_element(By.ID, "raise-1").click()
    time.sleep(2)
    driver.find_element(By.ID, "comments").send_keys("I am facing this issue")
    Select(driver.find_element(By.ID, "category")).select_by_visible_text("FEEDBACK")
    Select(driver.find_element(By.ID, "priority")).select_by_value("2")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="file"]').send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#Open-Other-Issue > div > div > form > div:nth-child(2) > button.btn.btn-primary").click()
    time.sleep(4)
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#global_Success_Message_Model_With_Id > div > div > div > div.row.mt-2.py-2.mb-2 > div > button")
    button.click()
    print("Issue created")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    edit_button = driver.find_element(By.CSS_SELECTOR, 'button.issue-edit-button')
    edit_button.click()
    comments = driver.find_element(By.NAME, 'comments')
    comments.send_keys("Adding a random comment for testing purposes.")
    priority = driver.find_element(By.NAME, 'priority')
    select = Select(priority)
    select.select_by_value('2')
    driver.find_element(By.ID, "files").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "/html/body/div[4]/div/div[9]/div/div[2]/div/div/div/form/div[1]/div[2]/button[3]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[26]/div/div/div/div[3]/div/button").click()
    time.sleep(2)
    feedback_tab = driver.find_element(By.ID, "feedback-tab")
    driver.execute_script("arguments[0].click();", feedback_tab)
    time.sleep(3)
    # ------------------------------------------------------
    button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[10]/div/div[1]/div[2]/button")

    driver.execute_script("arguments[0].click();",
                          button)  # filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.bg-white.text-primary

    time.sleep(5)
    # -------------------------------------------------------
    random_feedback = [
        "This is a random feedback message.",
        "I'm experiencing an issue with this.",
        "Great experience so far!",
        "This feature could use some improvement.",
        "Looking forward to future updates."
    ]

    # Choose a random feedback message
    feedback_text = random.choice(random_feedback)

    # Locate the feedback textarea
    feedback_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[12]/div/div/div[2]/form/div[3]/div/textarea"))
    )

    # Use JavaScript to set the value directly without clearing the placeholder
    driver.execute_script("arguments[0].value = arguments[1];", feedback_field, feedback_text)
    time.sleep(3)
    # ---------------------------------------------------------
    button = driver.find_element(By.XPATH, "/html/body/div[12]/div/div/div[2]/form/div[4]/div/button[2]")
    driver.execute_script("arguments[0].click();",
                          button)  # filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.bg-white.text-primary

    time.sleep(5)
    # ----------------------------------------------------------
    button = driver.find_element(By.XPATH, "/html/body/div[27]/div/div/div/div[4]/div/button")
    driver.execute_script("arguments[0].click();",
                          button)  # filterLeads > div > div.col-sm-9 > div > div.col-sm-4.d-flex.pt-4 > button.btn.bg-white.text-primary

    time.sleep(5)
    # -----------------------Scroll-------------------------------------
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    edit_button = driver.find_element(By.CLASS_NAME, 'feedback-edit-button')
    edit_button.click()

    # ---------------------------------------------
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # ------------------------------------------------
    driver.find_element(By.XPATH,
                        '/html/body/div[4]/div/div[10]/div/div[2]/div[1]/div/div/form/div[2]/div[3]/div[1]/div/select').click()

    # Locate the specific option by its value and click it
    option = driver.find_element(By.XPATH, "//select[@id='feedback-type']/option[@value='IMAGE']")
    option.click()

    feedback_textarea = driver.find_element(By.NAME, 'feedback')
    feedback_textarea.clear()
    feedback_textarea.send_keys("Please review my feedback and suggest improvements.")
    driver.find_element(By.ID, "feedback-files-1").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "/html/body/div[4]/div/div[10]/div/div[2]/div[1]/div/div/form/div[1]/div[2]/button[3]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[26]/div/div/div/div[3]/div/button").click()
    time.sleep(2)




