from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/explicit_wait2.html")
  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
  button = WebDriverWait(browser, 5).until(
      EC.element_to_be_clickable((By.ID, "book"))
  )
  button.click()
  browser.execute_script("window.scrollBy(0, 100);")
  x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
  x = x_element.text
  y = calc(x)
  input0 = browser.find_element(By.CSS_SELECTOR, '#answer')
  input0.send_keys(y)
  button1 = browser.find_element(By.ID, "solve")
  button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    