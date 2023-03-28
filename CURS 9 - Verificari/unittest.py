import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Test(TestCase):

    # In loc sa repetam elementele in fiecare test, le trecem aici o singura data si dupa le refelosim
    CHECK_BOX_1 = (By.ID,"checkbox-1")
    CHECK_BOX_2 = (By.ID,"checkbox-2")
    CHECK_BOX_3 = (By.ID,"checkbox-3")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(4)
        self.chrome.get("https://formy-project.herokuapp.com/")
        self.chrome.find_element(By.LINK_TEXT,"Checkbox").click()

    def tearDown(self):
        self.chrome.quit()

    #Numele metodelor de test trebuie OBLIGATORIU sa inceapa cu test
    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://formy-project.herokuapp.com/checkbox"
        assert actual_url == expected_url, f"Invalid url: expected:{expected_url}, actual: {actual_url}"


    # Varianta gresita de a verifica ca un element sa NU apara pe pagina
    @unittest.skip
    def test_element_not_displayed_v1(self):
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        # * tuple unpacking-  se ia valoarea din tuple si se da ca argument functiei
        element = self.chrome.find_element(*self.CHECK_BOX_1)
        # Daca nu facem unpack functia ar arata asa self.chrome.find_element((By.ID,"checkbox-1"))
        # Daca folosim unpack apelul functiei arata asa self.chrome.find_element(By.ID,"checkbox-1")
        assert element.is_displayed() == False, "Elementul este afisat"

    #Varianta Corecta
    def test_element_not_displayed_v2(self):
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        try:
            self.chrome.find_element(*self.CHECK_BOX_1)
            assert False, "Elementul este afisat"
        except NoSuchElementException:
            print("Elementul nu este afisat")