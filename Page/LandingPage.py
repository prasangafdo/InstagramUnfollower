import time

# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common import actions

from Page.LoginPage import *


class LandingPage(LoginPage):

    txtSearchBar = "//input[@aria-label='Search Input']"
    imgProfile = "//img[contains(@alt, 'profile pic')]//ancestor::div[@class='XrOey']"
    lnkProfile = "//div[contains(@class,'_7UhW9') and text()='Profile']"
    btnDirectMessage = "//a[contains(@aria-label,'Direct messaging')]"
    btnHome = "//*[name()='svg' and @aria-label='Home']/ancestor::a"
    btnAddToHomeCancel ="//button[text()='Cancel']"
    btnNotificationNotNow ="//button[text()='Not Now']"

    def isSearchBarDisplayed(self):
        time.sleep(5)
        return LoginPage.driver.find_element(By.XPATH, self.txtSearchBar).is_displayed()

    def endSession(self):
        LoginPage.driver.close()
        LandingPage.driver.quit()

    def navigateToProfile(self):
        LoginPage.driver.find_element(By.XPATH, self.imgProfile).click()
        LoginPage.driver.find_element(By.XPATH, self.lnkProfile).click()

    def openDirectMessages(self):
        LoginPage.driver.find_element(By.XPATH, self.btnDirectMessage).click()
        time.sleep(3)

    def navigateToHome(self):
        LoginPage.driver.find_element(By.XPATH, self.btnHome).click()
        time.sleep(4)

    def clickCancelFromAddToHomePopup(self):
        LoginPage.driver.find_element(By.XPATH, self.btnAddToHomeCancel).click()
        time.sleep(2)

    def clickNotNowFromEnableNotificationPopup(self):
        LoginPage.driver.find_element(By.XPATH, self.btnNotificationNotNow).click()
        time.sleep(4)


