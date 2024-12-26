import random
import datetime
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import databseConnection
from Functions import generate_random_date


def feedback(driver):
    driver.get("http://185.199.53.169:5000/feedbacks")
    time.sleep(2)

    #------------------Filters------------------------
    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "SELECT customer_name FROM feedbacks"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "search-input")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH, f"//div[@id='search-dropdown-content']//div[contains(text(), '{customer_name}')]").click()
    time.sleep(2)

    select_element = driver.find_element(By.ID, "feedbackValue")
    time.sleep(3)
    select = Select(select_element)
    options = [1, 2, 3, 4, 5]
    random_choice = random.choice(options)
    select.select_by_value(str(random_choice))

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

    button = driver.find_element(By.CSS_SELECTOR, "#feedback-filter > div > div.col-sm-2.d-flex.gap-1 > div:nth-child(2) > button")
    button.click()
    time.sleep(4)

    #----------------Reset all -------------------------------------------------------------------------
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div/form/div/div[3]/div[1]/button").click()
    time.sleep(2)
    #---------------------Create Feedback ---------------------------------------------------------------
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[1]/div[3]/button").click()
    time.sleep(3)

    query = "SELECT name FROM marketing_leads"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    time.sleep(3)
    search_input = driver.find_element(By.ID, "customerName")
    search_input.send_keys(customer_name)
    time.sleep(5)
    driver.find_element(By.XPATH,  f"//div[@id='username-dropdown-content']//div[contains(text(), '{customer_name}')]").click()
    time.sleep(2)

    random_rating = random.randint(1, 5)
    star_element = driver.find_element(By.CSS_SELECTOR, f"#star-rating i[data-feedback-value='{random_rating}']")
    star_element.click()

    driver.find_element(By.ID,"feedback-file").send_keys("C:/Users/bakal/OneDrive/Desktop/HC150.png")
    time.sleep(3)

    random_feedback = [
        "This is a random feedback message.",
        "I'm experiencing an issue with this.",
        "Great experience so far!",
        "This feature could use some improvement.",
        "Looking forward to future updates."
    ]

    # Choose a random feedback message
    feedback_text = random.choice(random_feedback)

    driver.find_element(By.NAME,"feedback").send_keys(feedback_text)
    time.sleep(3)
    # ----------------------------Save feedback-----------------------------
    driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/form/div[4]/div/button[2]").click()
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div/div[4]/div/button").click()
    time.sleep(5)
    # ------------------------Open particular data----------------------------------
    row = driver.find_element(By.CSS_SELECTOR, '#issuesTableBody tr:nth-child(1) td:nth-child(2)')
    row.click()
    time.sleep(5)

    driver.find_element(By.ID, "edit-btn").click()
    time.sleep(3)

    random_feedback = [
        "This is a random feedback message.",
        "I'm experiencing an issue with this.",
        "Great experience so far!",
        "This feature could use some improvement.",
        "Looking forward to future updates."
    ]

    # Choose a random feedback message
    feedback_text = random.choice(random_feedback)

    feedback=driver.find_element(By.NAME, "feedback")
    feedback.clear()
    feedback.send_keys(feedback_text)
    time.sleep(3)

    driver.find_element(By.ID, 'save-btn').click()
    time.sleep(3)

    driver.find_element(By.ID, "global_Success_Message_Btn").click()
    time.sleep(3)

    # -----------------------Feedback Screen-------------------------
    driver.find_element(By.ID,'feedback_button').click()
    time.sleep(3)



