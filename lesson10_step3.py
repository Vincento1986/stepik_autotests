from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  from selenium import webdriver
  from selenium.webdriver.common.by import By

  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/wait1.html")

  button = browser.find_element(By.ID, "verify")
  button.click()
  message = browser.find_element(By.ID, "verify_message")

  assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    