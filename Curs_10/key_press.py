import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class Keyborad(unittest.TestCase):

    INPUT_FIRST_NAME = (By.ID,"first-name")
    INPUT_LAST_NAME = (By.ID,"last-name")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://formy-project.herokuapp.com/form")

    def tearDown(self):
        self.chrome.quit()


    def test_pressing_keys(self):

        first_name = self.chrome.find_element(*self.INPUT_FIRST_NAME)

        first_name.send_keys("Valentin")
        sleep(1)
        first_name.send_keys(Keys.BACK_SPACE)
        sleep(1)
        first_name.send_keys(Keys.TAB)
        sleep(1)
        # ne folosim de action chains pentru a tine apasat pe o tasta si poi apasam alta tasta (tinem shift apasat si dupa tab)
        action = ActionChains(self.chrome)
        # folosind key_down tinem apasat pe tasta (SHIFT)
        action.key_down(Keys.SHIFT).perform()
        #apasam pe tasta TAB
        action.send_keys(Keys.TAB)

        #folosind key_up dam "drumul" la tasta SHIFT
        # daca nu punem si aceasta instrtiune de key_up si anterior am folosit key_down, nu va merge
        action.key_up(Keys.SHIFT).perform()
        sleep(1)
        first_name.send_keys(Keys.BACK_SPACE)
        sleep(2)
