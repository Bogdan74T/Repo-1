import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Alerts(unittest.TestCase):

    RESULT_MESSAGE = (By.ID,'result')
    ALERT_BUTTON = (By.XPATH,"//button[text()='Click for JS Alert']")
    CONFRIM_BUTTON = (By.XPATH,"//button[text()='Click for JS Confirm']")
    PROMPT_BUTTON = (By.XPATH,"//button[text()='Click for JS Prompt']")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.chrome.quit()

    def test_alert(self):
        self.chrome.find_element(*self.ALERT_BUTTON).click()

        obj = self.chrome.switch_to.alert # Ne-am mutat de pagina noastra pe fereastra de alerta
                                          # si am slavat fereastra de alerta intr-o variabila
        print(f"Mesajul din alerta {obj.text}")
        # sleep(2)
        obj.accept() # este echivalentul click-ului pe butonul "Ok" din alerta
        # sleep(3)
        expected_result = "You successfully clicked an alert"
        actual_result = self.chrome.find_element(*self.RESULT_MESSAGE).text
        # assert expected_result == actual_result, "Mesajul nu este cel dorit!"
        # sau
        self.assertEqual(expected_result,actual_result,"Mesajul nu este cel dorit!")

    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFRIM_BUTTON).click()
        obj = self.chrome.switch_to.alert
        print(f"Mesajul din confirm {obj.text}")

        # sleep(2)
        obj.accept()
        # sleep(2)

        expected_result = "You clicked: Ok"
        actual_result = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(expected_result,actual_result,"Mesajul nu este cel dorit!")

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFRIM_BUTTON).click()
        obj = self.chrome.switch_to.alert
        print(f"Mesajul din confirm {obj.text}")

        # sleep(2)
        obj.dismiss() # echivalentul click-ului pe butonul de Cancel din Confirm alert
        # sleep(2)

        expected_result = "You clicked: Cancel"
        actual_result = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(expected_result, actual_result, "Mesajul nu este cel dorit!")

    def test_prompt_text_ok(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()

        obj = self.chrome.switch_to.alert

        text = "TEST12"
        obj.send_keys(text)
        # sleep(3)
        obj.accept()
        # sleep(3)
        expected_result = f"You entered: {text}"
        actual_result = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(expected_result,actual_result,f"Mesajul asteptat este {expected_result}. Mesajul primit este {actual_result}")


    def test_prompt_cancel(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()

        obj = self.chrome.switch_to.alert

        text = "TEST12"
        obj.send_keys(text)
        # sleep(3)
        obj.dismiss()
        # sleep(3)
        expected_result = f"You entered: null"
        actual_result = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(expected_result, actual_result,
                         f"Mesajul asteptat este {expected_result}. Mesajul primit este {actual_result}")