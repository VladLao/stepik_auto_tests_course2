import os

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

input1 = browser.find_element(By.XPATH, "//input[@name='firstname']")
input1.send_keys("Ivan")

input2 = browser.find_element(By.XPATH, "//input[@name='lastname']")
input2.send_keys("Ivanov")

input3 = browser.find_element(By.XPATH, "//input[@name='email']")
input3.send_keys("Ivanov@ivan.list")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "text.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.XPATH, "//input[@name='file']")
element.send_keys(file_path)

button = browser.find_element(By.TAG_NAME, 'button')
button.click()
