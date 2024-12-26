import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://185.199.53.169:5000/sign-up")
time.sleep(2)
driver.find_element(By.ID,"firstName").send_keys("Kalyani")
driver.find_element(By.ID,"lastName").send_keys("Bakal")
driver.find_element(By.ID,"FEMALE").click()
driver.find_element(By.ID,"email").send_keys("kalyani@gmail.com")
driver.find_element(By.ID,"mobileNo").send_keys("9309574331")
driver.find_element(By.ID,"signUpPassword").send_keys("Kalyani@2006")
driver.find_element(By.ID,"signUpConfirmPassword").send_keys("Kalyani@2006")
time.sleep(2)
driver.execute_script("document.querySelector('button.btn.btn-primary.btn-block.form-control.mt-1').click();")
#http://185.199.53.169:5000/otp-verification
# driver.get("http://185.199.53.169:5000/otp-verification")
# time.sleep(2)
# driver.execute_script("document.querySelector('#f1').value = '2';")
# driver.execute_script("document.querySelector('#f2').value = '9';")
# driver.execute_scrip("document.querySelector('#f3').value = '6';")
# driver.execute_script("document.querySelector('#f4').value = '2';")
# driver.execute_script("document.querySelector('#f5').value = '3';")
# driver.execute_script("document.querySelector('#f6').value = '2';")
# submit_button = driver.find_element(By.ID, "submit")
# submit_button.click()
time.sleep(2)
driver.quit()