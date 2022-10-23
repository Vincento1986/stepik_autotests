from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
    y = math.log(abs(12 * math.sin(x)))
    return y

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)
    c = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, '#answer')
    y_element.send_keys(c)
    rob_element = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    rob_element.click()
    rule_element = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rule_element)
    rule_element.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()    

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    