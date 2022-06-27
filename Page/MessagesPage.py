from Page.LoginPage import *


class MessagesPage(LoginPage):

    btnMessageRequests = "// h5[contains(text(),'Request')] / parent::button"
    # btnUserName = "// div[text() = 'user display name'] / ancestor::a"
    btnUserName = "// div[text() = 'Anjulee Fernando'] / ancestor::a"
    def openMessageRequests(self):
        LoginPage.driver.find_element(By.XPATH, self.btnMessageRequests).click()
        time.sleep(3)

    def endSession(self):
        LoginPage.driver.close()
        # LandingPage.driver.quit()

    def scrollToTop(self):
        LoginPage.driver.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")

    def openUserThread(self):
        LoginPage.driver.find_element(By.XPATH, self.btnUserName).click()
        time.sleep(5)
