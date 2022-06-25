from Page.LoginPage import *


class MessagesPage(LoginPage):

    btnMessageRequests = "// h5[contains(text(),'Request')] / parent::button"
    # btnUserName = "// div[text() = 'user display name'] / ancestor::a"
    btnUserName = "// div[text() = 'Anjulee Fernando'] / ancestor::a"

    def openMessageRequests(self):
        LoginPage.driver.find_element(By.XPATH, self.btnMessageRequests).click()

    def endSession(self):
        LoginPage.driver.close()
        # LandingPage.driver.quit()

