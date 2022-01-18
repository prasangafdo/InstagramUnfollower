from Page.LoginPage import *


class AccountPage(LoginPage):

    lblFollowingCount = "//a[contains(@href,'following')]/span"
    lblFollowersCount = "//a[contains(@href,'followers')]/span"
    lstFollowing = "//div[@class='isgrP']"
    lblFollowingListLoader = "//li[@class='wo9IH QN7kB ']/div/*[name()='svg']"
    lnkFollowing = "//a[contains(@href,'following')]"

    def getFollowingCount(self):
        time.sleep(3)
        print("You're following : ", LoginPage.driver.find_element(By.XPATH, self.lblFollowingCount).text)
        # return LoginPage.driver.find_element(By.XPATH, self.lblFollowingCount).get_text()


    def getFollowersCount(self):
        time.sleep(3)
        print("You're followed by : ", LoginPage.driver.find_element(By.XPATH, self.lblFollowersCount).text)


    # def getFollowersCount(self):
    #     time.sleep(3)
    #     LoginPage.driver.find_element(By.XPATH, self.lnkFollowing).click()
    #     # self.moveMouseCursor()
