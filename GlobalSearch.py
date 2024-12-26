import datetime
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

import databseConnection


def global_search(driver):
    driver.find_element(By.ID,"settings-icon").click()
    time.sleep(3)

    # name_radio = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="name"]')
    # name_radio.click()
    # assert name_radio.is_selected(), "The 'Name' radio button should be selected."
    #
    id_radio = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="id"]')
    id_radio.click()
    assert id_radio.is_selected(),"The 'ID' radio button should be selected."

    # skip=driver.find_element(By.NAME, "skip")
    # skip.send_keys(3)
    # time.sleep(3)
    #
    # top=driver.find_element(By.NAME, "top").click()
    # top.send_keys(2)
    # time.sleep(3)
    #
    apply_button = driver.find_element(By.XPATH, "//button[text()='Apply']")
    apply_button.click()
    #
    # apply_button = driver.find_element(By.XPATH, "//button[text()='Cancle']")
    # apply_button.click()
    #
    # close_button = driver.find_element(By.XPATH, "//a[@onclick='toggleRightMenu()' and text()='×']")
    # close_button.click()
    time.sleep(3)
    ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
    ok_button.click()
    time.sleep(3)
    connection = databseConnection.conn()
    cursor = connection.cursor()
    query = "SELECT entity_id FROM global_search"
    cursor.execute(query)
    result = cursor.fetchall()
    customer_name = result[0][0]
    print(customer_name)
    search_input = driver.find_element(By.ID, "global-search")
    search_input.send_keys(customer_name)
    time.sleep(3)
    driver.find_element(By.XPATH, f"//div[@id='global-dropdown-content']//div[contains(text(), '{customer_name}')]").click()
    time.sleep(3)
