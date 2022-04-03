from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
driver = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)

   option1 = browser.find_element_by_xpath("//img[@id='treasure']")
   option2 = option1.get_attribute("valuex")
   x = option2
   y = calc(x)

   input1 = browser.find_element_by_id("answer")
   input1.send_keys(y)

   option3 = browser.find_element_by_id("robotCheckbox")
   option3.click()
   option4 = browser.find_element_by_xpath("//input[@id='robotsRule']")
   option4.click()
   button = browser.find_element_by_css_selector("button.btn")
   button.click()


finally:
   # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()