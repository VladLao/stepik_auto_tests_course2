from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

option1 = browser.find_element_by_xpath("//span[@id='input_value']")
x = option1.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option3 = browser.find_element_by_id("robotCheckbox").click()
option4 = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", option4)
option4.click()

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()