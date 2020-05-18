from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(5)
actions = ActionChains(driver)
driver.get("https://www.apple.com/")
iphone = driver.find_element_by_css_selector("[href='/iphone/']")
# Select top level iphone icon
actions.move_to_element(iphone).perform()
actions.click(iphone).perform()
driver.maximize_window()
iphones = driver.find_elements_by_xpath("//span[@class='chapternav-label'][contains(text(),'iPhone')]")
str = []
item = -1
for phone in iphones:
    str.append(phone.text)
    item = item + 1
    if (phone.text == 'iPhone SE'):
        phone.click()
        print("clicked on", str[item])
        break

print("List of iPhones on the homepage", str)

driver.find_element_by_css_selector("[data-analytics-title='buy iphone se']").click()
driver.find_element_by_css_selector("[for='noTradeIn']").click()
driver.find_element_by_css_selector("[id='Item1product_red_label']").click()

print(driver.find_element_by_xpath("//h2[contains(text(),'capacity')]").text)
capacity = driver.find_element_by_css_selector("[for*='128gb']")
actions.move_to_element(capacity).perform()
actions.click(capacity).perform()


