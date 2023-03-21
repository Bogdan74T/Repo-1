import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("http://www.seleniumframework.com/Practiceform/")
chrome.find_element(By.NAME,"country").send_keys("Romania")
chrome.find_element(By.NAME,"company").send_keys("IT Factory")

# am gasit 2 elemente cu name=email

#daca exista mai multe elemente cu acelasi crteriu (name="email") si folosim find_element, va fi luat primul element gasit pe pagina tot timpul
# chrome.find_element(By.NAME,"email").send_keys("asdad@mail.com")

#cu find_elements facem rost de toate elementele care respecta un anumit criteriu (ex: name="email")
chrome.find_elements(By.NAME,"email")[0].send_keys("mail1@mail.com")

chrome.find_elements(By.NAME,"email")[1].send_keys("mail2@mail.com")

time.sleep(5)
chrome.quit()