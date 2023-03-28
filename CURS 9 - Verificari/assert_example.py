from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome  = webdriver.Chrome()

chrome.get("https://formy-project.herokuapp.com/checkbox")

actual_url = chrome.current_url

expected_url = "https://formy-project.herokuapp.com/checkbox"

assert actual_url == expected_url, f"Invalid url: expected:{expected_url}, actual: {actual_url}"

print("Executia continua")
chrome.quit()