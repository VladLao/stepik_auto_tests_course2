import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

button = browser.find_element(By.TAG_NAME, 'button')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = int(browser.find_element(By.ID, 'input_value').text)

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(str(math.log(abs(12 * math.sin(x)))))

button = browser.find_element(By.TAG_NAME, 'button')
button.click()
