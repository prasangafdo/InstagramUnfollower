import time

from Page.LoginPage import *


class LandingPage(LoginPage):

    txtSearchBar = "//input[@aria-label='Search Input']"
    imgProfile = "//img[contains(@alt, 'profile pic')]//ancestor::div[@class='XrOey']"
    lnkProfile = "//div[contains(@class,'_7UhW9') and text()='Profile']"
    lnkFollowing = "//a[contains(@href,'following')]"
    lblFollowingCount = "//a[contains(@href,'following')]/span"
    lblFollowersCount = "//a[contains(@href,'followers')]/span"


    def isSearchBarDisplayed(self):
        time.sleep(5)
        return LoginPage.driver.find_element(By.XPATH, self.txtSearchBar).is_displayed()

    def endSession(self):
        LoginPage.driver.close()
        LandingPage.driver.quit()

    def navigateToProfile(self):
        LoginPage.driver.find_element(By.XPATH, self.imgProfile).click()
        LoginPage.driver.find_element(By.XPATH, self.lnkProfile).click()

    def getFollowingCount(self):
        time.sleep(3)
        print("You're following : ", LoginPage.driver.find_element(By.XPATH, self.lblFollowingCount).text)
        # return LoginPage.driver.find_element(By.XPATH, self.lblFollowingCount).get_text()

    def getFollowersCount(self):
        time.sleep(3)
        print("You're followed by : ", LoginPage.driver.find_element(By.XPATH, self.lblFollowersCount).text)
