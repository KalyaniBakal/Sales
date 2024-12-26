import random
import string
import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import databseConnection

def couponMangemnet(driver):
    driver.get("http://185.199.53.169:5000/admin")
    time.sleep(2)
    # cache_management = driver.find_element(By.CSS_SELECTOR, "div.col-sm-12.py-2.mt-2.bg-white.rounded-1.task-row")
    # cache_management.click()
    # time.sleep(2)
    # clear_cache_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    # clear_cache_button.click()
    # time.sleep(3)
    # ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
    # ok_button.click()
    # time.sleep(3)
    # element = driver.find_element(By.CSS_SELECTOR, "div.pointer.text-secondary.cursor")
    # element.click()
    # time.sleep(3)
    #
    element = driver.find_element(By.XPATH, "//h4[text()='Coupon Management']")
    element.click()
    time.sleep(3)

    # connection = databseConnection.conn()
    # cursor = connection.cursor()
    # query = "select name from coupons;"
    # cursor.execute(query)
    # result = cursor.fetchall()
    # customer_name = result[0][0]
    # print(customer_name)
    # search_input = driver.find_element(By.NAME, "name")
    # search_input.send_keys(customer_name)
    # time.sleep(3)
    #
    # reset_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    # reset_button.click()
    # time.sleep(3)

    bulk = driver.find_element(By.ID, "bulk-action")
    bulk.click()
    time.sleep(3)

    change_date_item = driver.find_element(By.XPATH, "//div[text()='Change Date' and contains(@class, 'dropdown-item')]")
    change_date_item.click()


