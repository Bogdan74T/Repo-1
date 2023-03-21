import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")


chrome.find_element(By.CLASS_NAME,"form-control").send_keys("FIRSTNAME_BY_CLASS")

chrome.find_elements(By.CLASS_NAME,"form-control")[2].send_keys("JOB_BY_CLASS")

# pot sa selectez o optiune dintr-un dropdown
chrome.find_elements(By.CLASS_NAME,"form-control")[3].click()


# prin clasa Select selectam o optiune dintr-un dropdown prin textul vizibil de pe site al optiunii
Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_visible_text("5-9")
time.sleep(1)
Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_index(1)
time.sleep(1)
Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_value("4")
time.sleep(4)
chrome.quit()