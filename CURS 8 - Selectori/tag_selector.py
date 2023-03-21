import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")



chrome.find_element(By.TAG_NAME,"input").send_keys("FIRSTNAME")

#accesam al 3-lea element prin index [2]
chrome.find_elements(By.TAG_NAME,"input")[2].send_keys("PROGRAMATOR")
time.sleep(4)
chrome.quit()