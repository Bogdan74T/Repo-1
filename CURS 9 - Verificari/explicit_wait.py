from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome  = webdriver.Chrome()

chrome.get("https://formy-project.herokuapp.com/checkbox")

chrome.implicitly_wait(5)
#va astepta maxim 5 secunde pana gasete elementul
chrome.find_element(By.ID,"checkbox-20")

# Explicit wait
# Asteptam maxim 15 de secunde strict dupa elementul cu id-ul 'checkbox-12'
check_box = WebDriverWait(chrome,15).until(EC.presence_of_element_located((By.ID,"checkbox-12")))
check_box.click()

#va astepta maxim 5 secunde pana gasete elementul
chrome.find_element(By.ID,"checkbox-1")
# sleep(4)
chrome.quit()