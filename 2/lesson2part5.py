from selenium import webdriver
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
driver = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)

   option1 = browser.find_element_by_xpath("//span[@id='input_value']")
   x = option1.text
   y = calc(x)

   input1 = browser.find_element_by_id("answer")
   input1.send_keys(y)

   option2 = browser.find_element_by_id("robotCheckbox")
   option2.click()
   option3 = browser.find_element_by_xpath("//input[@id='robotsRule']")
   option3.click()
   button = browser.find_element_by_css_selector("button.btn")
   button.click()


finally:
   # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()