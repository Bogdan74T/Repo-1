import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ContextMenu(unittest.TestCase):

    CONTEXT = (By.ID, "hot-spot")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/context_menu")

    def tearDown(self):
        self.chrome.quit()


    def test_context(self):
        context_box = self.chrome.find_element(*self.CONTEXT)

        # folosind click() facem click stanga, click-ul normal
        context_box.click()

        # action chains ne ajuta sa facem click dreapta
        # un alt exemplu: action chains ne poate ajuta cand avem nevoie sa tinem apasat pe un buton si de exemplu in acelasi timp sa facem click
        action = ActionChains(self.chrome)

        # metoda context_click ne ajuta sa definim un context in care noi putem sa facem click dreapta
        # fara metoda context_clicl nu putem accesa metoda perfom() care executa comanda de click dreapta in acest caz
        sleep(2)
        action.context_click(context_box).perform()
        sleep(3)
        self.chrome.switch_to.alert.accept()
        sleep(2)