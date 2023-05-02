from time import sleep

from selenium import webdriver
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as BraveService
#CHROME
# pentru a rula teste pe Chrome, cu versiunea de selenium 4.6.0+
# driver  = webdriver.Chrome()
#pentru versiunile mai vechi de selenium
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Firefox
# pentru a rula teste pe Chrome, cu versiunea de selenium 4.6.0+
# driver = webdriver.Firefox()
# pentru versiunile mai vechi de selenium
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#Brave
driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

sleep(5)
driver.quit()