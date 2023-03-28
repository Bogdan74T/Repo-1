from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome  = webdriver.Chrome()

chrome.get("https://formy-project.herokuapp.com/radiobutton")

# Exemplu: vrem sa cautam un element cu xpath-ul "//label[@for='radio-button-1']" de pe pagina
# Sistemul va cauta acel element, si daca il gaseste, va trece instant la urmatoarea instuctiune

# Daca nu il gaseste sistemul va continua sa-l caute pe toata durata stabilita de implicit wait
# si daca nu il gaseste pana la finalul perioadei, va returna eroare (exemplul de mai jos,
# cauta maxim 5 secunde dupa fiecare element cautat)

## Atentie daca nu avem acel implicit wait, atunic va returna eroare instant

#AICI NU SE CAUTA TIMP DE 5 SECUNDE PENTRU A FI GASIT ELEMENTUL
label_text = chrome.find_element(By.XPATH,"//label[@for='radio-button-3']").text
print(label_text)

# De aici in jos se va cauta timp de 5 secunde pentru fiecare element pentru a-l gasi
chrome.implicitly_wait(5)

label_text = chrome.find_element(By.XPATH,"//label[@for='radio-button-1']").text
print(label_text)

# chrome.find_element(By.XPATH, "//label[@for='radio-button-13']")

label_text_2 = chrome.find_element(By.XPATH,"//label[@for='radio-button-2']").text
print(label_text_2)

chrome.quit()

"""
Setam implicit wait in secunde:
    - o modalitate prin care definim un timp global de asteptare pana cand sa dea eroarea cand elementul
    nu a fost gasit
    - se va instantia in momentul in care va fi executata instructiunea implicitly_wait(x) 
    si va fi distrus in momentul in care exectia se incheie si browserul se inchide

Selenium va cauta toate elementele maxim 'x' secunde.

Diferenta intre implicit wait si sleep eca ca instructiunea de sleep va "astepta" orice ar fi 
(indiferent daca gaseste elementul sau nu) (opreste din executie tot codul)
iar implicit wait continua cautarea in acel numar de secunde pana gaseste elementul.
"""