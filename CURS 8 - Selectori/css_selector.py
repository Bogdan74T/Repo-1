import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.CSS_SELECTOR,"input#first-name").send_keys("TEST@@@@@@@@")
# chrome.find_element(By.CSS_SELECTOR,"select#select-menu").click()
chrome.find_element(By.CSS_SELECTOR,"select.form-control").click()
#<input type="text" class="form-control" id="last-name" placeholder="Enter last name">
chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("PRENUME")

#<input type="text" class="form-control" id="job-title" placeholder="Enter your job title">
chrome.find_element(By.CSS_SELECTOR,"input[placeholder*='job title']").send_keys("JOB")

time.sleep(4)
chrome.quit()