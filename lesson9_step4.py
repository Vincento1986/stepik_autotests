from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x.text
    y = calc(x)
    inp = browser.find_element(By.CSS_SELECTOR, "#answer")
    inp.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    