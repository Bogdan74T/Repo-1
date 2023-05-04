from selenium.webdriver.common.by import By

from browser import Browser

# in aceasta pagina punem toate metodele si elementele utile in orice pagina si
# nu neaparat specifice unei anumite pagini.
class BasePage(Browser):

    COMMERCE_LOGO = (By.XPATH,"//a/img")

    def check_the_current_url(self, url):
        actual = self.driver.current_url
        assert actual == url ,f"Url-ul este gresit"
