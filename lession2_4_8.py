from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
import time

def calc(y):
    return str(log(abs(12*sin(y))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID,'book')
    x = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),'100'))
    button.click()
    
    y = int(browser.find_element(By.ID,'input_value').text)
    browser.find_element(By.ID,'answer').send_keys(calc(y))
    button = browser.find_element(By.ID,'solve').click()
    
finally:
    time.sleep(10)
    browser.quit()