import time

from Page.LoginPage import *


class LandingPage(LoginPage):

    txtSearchBar = "//input[@aria-label='Search Input']"

    def isSearchBarDisplayed(self):
        time.sleep(5)
        return LoginPage.driver.find_element(By.XPATH, self.txtSearchBar).is_displayed()

    def endSession(self):
        LoginPage.driver.close()
        LandingPage.driver.quit()