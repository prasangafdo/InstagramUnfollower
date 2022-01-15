from Page.LoginPage import *


class LandingPage(LoginPage):

    txtSearchBar = "//input[@aria-label='Search Input']"

    def isSearchBarDisplayed(self):
        return LoginPage.driver.find_element(By.XPATH, self.txtSearchBar).is_displayed()