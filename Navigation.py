import time
from selenium.webdriver.common.by import By
import logging

def navigation(driver):
    time.sleep(3)
    driver.find_element(By.ID,"Leads_button").click()
    print("Move to Lead Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "static_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    healers_link = driver.find_element(By.LINK_TEXT, "Healers")
    healers_link.click()  # Click on 'Healers'
    time.sleep(3)
    print("Move to Healers Screen")
    logging.info("Move to Healers Screen.")

    submenu = driver.find_element(By.ID, "static_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    remedies_link = driver.find_element(By.LINK_TEXT, "Remedies")
    remedies_link.click()  # Click on 'Remedies'
    time.sleep(3)
    print("Move to Remedy Screen")

    submenu = driver.find_element(By.ID, "static_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    offerings_link = driver.find_element(By.LINK_TEXT, "Offeringsss")
    offerings_link.click()
    time.sleep(3)
    print("Move to Offering Screen")

    submenu = driver.find_element(By.ID, "static_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    addresses_link = driver.find_element(By.LINK_TEXT, "Addresses")
    addresses_link.click()
    time.sleep(3)
    print("Move to Address Screen")

    submenu = driver.find_element(By.ID, "static_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    categories_link = driver.find_element(By.LINK_TEXT, "Category")
    categories_link.click()
    print("Move to Category Screen")
    time.sleep(3)

    driver.find_element(By.ID, "users_button").click()
    print("Move to Users Screen")
    time.sleep(3)

    driver.find_element(By.ID, "consultation_button").click()
    print("Move to Consultation Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    sales_report_link = driver.find_element(By.LINK_TEXT, "Sales report")
    sales_report_link.click()
    print("Move to Sales report Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    agent_conversion_report_link = driver.find_element(By.LINK_TEXT, "Agent conversion report")
    agent_conversion_report_link.click()
    print("Move to Agent conversion report Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    consultation_schedule_report_link = driver.find_element(By.LINK_TEXT, "Consultation schedule report")
    consultation_schedule_report_link.click()
    print("Move to Consultation schedule report Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    free_healing_report_link = driver.find_element(By.LINK_TEXT, "Free Healing report")
    free_healing_report_link.click()
    print("Move to Free Healing report Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    healer_schedule_report_link = driver.find_element(By.LINK_TEXT, "Healer schedule report")
    healer_schedule_report_link.click()
    print("Move to Healer schedule report Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    extension_report_link = driver.find_element(By.LINK_TEXT, "Extension report")
    extension_report_link.click()
    print("Move to Extension report Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    recovery_report_link = driver.find_element(By.LINK_TEXT, "Recovery report")
    recovery_report_link.click()
    print("Move to Recovery report Screen")
    time.sleep(3)

    submenu = driver.find_element(By.ID, "Reports_submenu")
    driver.execute_script("arguments[0].style.display = 'block';", submenu)

    top_customers_report_link = driver.find_element(By.LINK_TEXT, "Top customers report")
    top_customers_report_link.click()
    print("Move to Top customers report Screen")
    time.sleep(3)

    driver.find_element(By.ID, "issues_button").click()
    print("Move to Issues Screen")
    time.sleep(3)

    driver.find_element(By.ID, "feedback_button").click()
    print("Move to Feedback Screen")
    time.sleep(3)

    driver.find_element(By.ID, "booking_button").click()
    print("Move to Booking Screen")
    time.sleep(3)

    driver.find_element(By.ID, "files_button").click()
    print("Move to Files Screen")
    time.sleep(3)

    driver.find_element(By.ID, "emi_button").click()
    print("Move to EMI Screen")
    time.sleep(3)

    driver.find_element(By.ID, "Calls_button").click()
    print("Move to Calls Screen")
    time.sleep(3)

    driver.find_element(By.ID, "healing_button").click()
    print("Move to Healing Screen")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button//p[text()='Jobs']").click()
    print("Move to Jobs Screen")
    time.sleep(3)

    driver.find_element(By.ID, "coupon_button").click()
    print("Move to Calls Screen")
    time.sleep(3)

    driver.find_element(By.ID, "tasks_button").click()
    print("Move to Calls Screen")
    time.sleep(3)

    driver.find_element(By.XPATH, "//p[text()='Admin']")
    print("Move to Admin Screen")
    time.sleep(3)

