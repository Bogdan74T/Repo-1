"""
Selectia elementelor in pagina cu linkText idetifica hyperlink-urile <a> din HTML
folosind text-ul afisat in pagina.
Textul trebuie sa se potriveasca 100% cu text-ul de la <a> folosit in codul HTML al paginii pe care o testam.

EX:
<a class="btn btn-lg" href="/autocomplete">Autocomplete</a>

a = este tagul care defineste un element de tip ancora (adica link catre alta pagina)
href = link-ul efectiv catre care se navigheaza. (Deobicei nu se pune link-ul complet (cum vedem in browser))
link complet:https://formy-project.herokuapp.com/autocomplete
domeniu- https://formy-project.herokuapp.com
extensia - /autocomplete

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com")


chrome.find_element(By.LINK_TEXT,"Autocomplete").click()
time.sleep(3)
chrome.find_element(By.ID, "logo").click()

time.sleep(3)
chrome.find_element(By.LINK_TEXT,"Buttons").click()

time.sleep(3)

try:
    chrome.find_element(By.LINK_TEXT,"Autocomplete").click()
except:
    print("Elementul nu a fost gasit")

chrome.quit()