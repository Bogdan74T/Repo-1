import unittest

import HtmlTestRunner

from Curs_10.alerts import Alerts
from Curs_10.auth import Auth
from Curs_10.context_menu import ContextMenu
from Curs_10.key_press import Keyborad
from Curs_9.unittests import Test


class TestSuite(unittest.TestCase):

    # numele metodei este predefinit si NU trebuie schimbat
    def test_suite(self):

        #am creat un obiect al clasei TestSuite
        #prin obiectul creat test_to_run vom avea acces la metoda addTests
        test_to_run = unittest.TestSuite()

        #metoda addTests primeste ca parametru o lista de teste care se doreste a fi executate
        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Auth),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyborad),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test)
        ])

        #Facem un test runnner HTML care va genera pentru noi niste rapoarte
        # Raportul este human-friendly si poate fi inteles de catre persoane care nu au scris/cunosc codul testelor
        runner = HtmlTestRunner.HTMLTestRunner(
            # combine_reports=True,
            report_name = "First_report",
            report_title="First_report"
        )
        runner.run(test_to_run)