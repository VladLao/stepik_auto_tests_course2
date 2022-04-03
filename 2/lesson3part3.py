from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(str(int(x)+int(y)))
driver = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element_by_xpath("//span[@id='num1']")
    option2 = browser.find_element_by_xpath("//span[@id='num2']")
    x = option1.text
    y = option2.text
    z = calc(x)
    select = Select(browser.find_element_by_xpath("//select[@id]"))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(30)
    browser.quit()
