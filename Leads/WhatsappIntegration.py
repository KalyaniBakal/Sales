import string
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def WhatsappIntegration(driver):
    driver.get("http://185.199.53.169:5000/marketing-leads")
    time.sleep(3)

    qr_code_button = driver.find_element(By.XPATH, "//button[contains(text(), 'QR Code')]")
    qr_code_button.click()
    time.sleep(2)
    # --------------------------------------

    whatsapp_button = driver.find_element(By.ID, "whatsapphref")
    ActionChains(driver).move_to_element(whatsapp_button).perform()
    time.sleep(1)
    whatsapp_button.click()
    print("Clicked the WhatsApp Share button.")

    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    print("Switched to WhatsApp window.")

    expected_url = "https://api.whatsapp.com/send?text=http%3A%2F%2F185.199.53.169%3A5000%2Fpublic%2Fnew-lead"
    current_url = driver.current_url
    if expected_url in current_url:
        print("WhatsApp share URL is correct.")
        driver.switch_to.window(driver.window_handles[0])
    else:
        print(f"Unexpected URL: {current_url}")

    driver.find_element(By.XPATH, "/html/body/div[6]/div/div/form/div[2]/button[1]").click()
    time.sleep(2)
    print("Cancel button clicked successfully!")

