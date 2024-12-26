import logging
import time
from selenium.webdriver.common.by import By

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def logout(driver):
    driver.find_element(By.ID, "logout").click()  # Logout button click
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div/button").click()
    logging.info("Logged out successfully")
    time.sleep(1)
