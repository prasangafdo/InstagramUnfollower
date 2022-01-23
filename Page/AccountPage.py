import time

from selenium.webdriver import ActionChains, Keys

from Page.LoginPage import *


class AccountPage(LoginPage):
    lblFollowingCount = "//a[contains(@href,'following')]/span"
    lblFollowersCount = "//a[contains(@href,'followers')]/span"
    lblFollowingListLoader = "//li[@class='wo9IH QN7kB ']/div/*[name()='svg']"
    lnkFollowing = "//a[contains(@href,'following')]"
    lnkFollowers = "//a[contains(@href,'followers')]"
    lblFollowingPopUp = "//div[@aria-label='Following']"
    lblFollowingList = "//a[contains(@class,'FPmhX notranslate')]"
    lblFollowersList = "//a[contains(@class,'FPmhX notranslate')]"

    lstFollowing = []
    lstFollowers = []
    lstIGMembersNotFollowingBack = []

    # mmm = "//a[@href='/ruu_1111/']"
    # mmm = "(//div[@class='PZuss']/li)[1]"
    mmm = "//ul[@class=' jjbaz _6xe7A']"


    def getFollowingCount(self):
        time.sleep(3)
        print("You're following : ", LoginPage.driver.find_element(By.XPATH, self.lblFollowingCount).text)
        # return LoginPage.driver.find_element(By.XPATH, self.lblFollowingCount).get_text()

    def getFollowersCount(self):
        time.sleep(3)
        print("You're followed by : ", LoginPage.driver.find_element(By.XPATH, self.lblFollowersCount).text)

    def clickOnFollowingLink(self):
        time.sleep(3)
        LoginPage.driver.find_element(By.XPATH, self.lnkFollowing).click()

    def clickOnFollowersLink(self):
        time.sleep(3)
        LoginPage.driver.find_element(By.XPATH, self.lnkFollowers).click()

    def scrollDownTheList(self):
        time.sleep(10)
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = LoginPage.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            LoginPage.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = LoginPage.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def navigateToAccountByURL(self, endpoint):
        time.sleep(1)
        url = "https://www.instagram.com/" + endpoint
        LoginPage.driver.get(url)

    def isLoadingDisplayed(self):
        return LoginPage.driver.find_element(By.XPATH, self.lblFollowingListLoader).is_displayed()

    def getFollowingList(self):
        time.sleep(2)
        for user in LoginPage.driver.find_elements(By.XPATH, self.lblFollowingList):
            print(user.text)
            self.lstFollowing.append(user.text)

    def getFollowersList(self):
        time.sleep(2)
        for user in LoginPage.driver.find_elements(By.XPATH, self.lblFollowersList):
            print(user.text)
            self.lstFollowers.append(user.text)

    def getIGMembersWhoFollowYouBack(self):
        print("--------Good people---------")
        for val1 in self.lstFollowing:
            for val2 in self.lstFollowers:
                if val1 == val2:
                    print(val1)
        print("--End of good people")

    def getIGMembersWhoDontFollowYouBack(self):
        print("--------Bad people---------")
        for val1 in self.lstFollowing:
            for val2 in self.lstFollowers:
                if val1 == val2:
                    print(val1)
        print("--End of bad people")