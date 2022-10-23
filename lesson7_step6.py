from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element1 = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x_element = x_element1.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input0 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input0.send_keys(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input1.click()
    input2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    input2.click()
    time.sleep(1)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    