from selenium.webdriver import ActionChains, Keys

from Page.LoginPage import *


class MessagesPage(LoginPage):

    btnMessageRequests = "// h5[contains(text(),'Request')] / parent::button"
    # btnUserName = "// div[text() = 'user display name'] / ancestor::a"
    btnUserName = "// div[text() = 'Anjulee Fernando'] / ancestor::a"
    lblMessage = "//div[@class='_acd2 _acd3']//div[@role='button']"
    lblChatContainer = "//div[@class='_ab8w  _ab94 _ab99 _ab9g _ab9m _ab9o']"



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
        time.sleep(3)

    def touchAndHoldAmessage(self):
        ActionChains(LoginPage.driver).click_and_hold(self.lblMessage).perform()

    def scrollUp(self):
        LoginPage.driver.find_element(By.XPATH, self.lblChatContainer).click()
        # LoginPage.driver.find_element(By.XPATH, self.lblChatContainer).
        action = ActionChains(LoginPage.driver)

        # perform the operation
        action.key_down(LoginPage.driver).send_keys('a').key_up(Keys.UP).perform()