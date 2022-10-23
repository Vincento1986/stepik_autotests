from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_element = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_element.send_keys("Gfgf")
    last_element = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_element.send_keys("hhh")
    email_element = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email_element.send_keys("hdddddddd")
    email_element.click()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    up_element = browser.find_element(By.CSS_SELECTOR, "#file")
    up_element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    