"""
Ex element HTML:
<input type="text" class="form-control" id="first-name" placeholder="Enter first name">

id = atributul
"first-name"-valoarea atributului

(
class = atribut
"form-control" - valoarea atributului
)
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initializam chrome-ul
# Acest lucru ne va deschide un now browser de chrome cu care vom interactiona
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")      # cu metoda .get() navigam spre link-ul pus intre ghilimele


prenume = chrome.find_element(By.ID,"last-name")
# metoda send_keys  este o meotda pe care o folosim sa scriem intr-un cam din pagina
prenume.send_keys("Popescu")

# metoda chaining ( in lant)
chrome.find_element(By.ID, "first-name").send_keys("Valentin")

time.sleep(3)

prenume.clear()

time.sleep(5) # astepta 5 secunde pentru a putea vizualiza ce se intampla (codul executandu-se prea repede pentru a putea observa cu ochiul liber)


chrome.quit()       # metoda folosita pentru a inchide browser-ul

# chrome.close()      # metoda care inchide tab-ul curent