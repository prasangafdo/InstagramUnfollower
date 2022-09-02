import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page.LoginPage import *


class AccountPage(LoginPage):
    lblFollowingCount = "//div[contains(text(),'following')]/span"
    lblFollowersCount = "//div[contains(text(),'followers')]/span"
    lblFollowingListLoader = "//li[@class='wo9IH QN7kB ']/div/*[name()='svg']"
    lnkFollowing = "//a[contains(@href,'following')]"
    lnkFollowers = "//a[contains(@href,'followers')]"
    lblFollowingPopUp = "//div[@aria-label='Following']"
    lblFollowingList = "//a[contains(@class,'notranslate')]/span"
    lblFollowersList = "//a[contains(@class,'notranslate')]/span"
    btnUnfollow = "//span[contains(@class,'glyphsSpriteFriend_Follow')]/ancestor::button"
    btnFollow = "//button[text()='Follow']"

    btnUnfollowInPopup = "//button[contains(@class,'-Cab_') and text()='Unfollow']"  # Add a click to this element
    # and add a verification point

    driver = LoginPage.driver

    lstFollowing = []
    lstFollowers = []
    lstIGMembersNotFollowingBack = []

    lstExcept = []

    # mmm = "//a[@href='/ruu_1111/']"
    # mmm = "(//div[@class='PZuss']/li)[1]"
    mmm = "//ul[@class=' jjbaz _6xe7A']"

    def getFollowingCount(self):
        time.sleep(3)
        print("You're following : ", self.driver.find_element(By.XPATH, self.lblFollowingCount).text)
        # return LoginPage.driver.find_element(By.XPATH, self.lblFollowingCount).get_text()

    def getFollowersCount(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.lblFollowersCount)))
        print("You're followed by : ", self.driver.find_element(By.XPATH, self.lblFollowersCount).text)

    def clickOnFollowingLink(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.lnkFollowing).click()

    def clickOnFollowersLink(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.lnkFollowers)))
        self.driver.find_element(By.XPATH, self.lnkFollowers).click()

    def scrollDownTheList(self):
        time.sleep(10)
        # SCROLL_PAUSE_TIME = 2
        #
        # # Get scroll height
        # last_height = self.driver.execute_script("return document.body.scrollHeight")
        #
        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     # Wait to load page
        #     time.sleep(SCROLL_PAUSE_TIME)
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        element = self.driver.find_element(By.XPATH, self.lblFollowingList)
        ActionChains(self.driver).click_and_hold(element)
        ActionChains(self.driver).move_by_offset(13, 15).perform()



    def navigate_to_account_by_url(self, endpoint):
        time.sleep(1)
        url = "https://www.instagram.com/" + endpoint
        self.driver.get(url)
        time.sleep(5)

    def isLoadingDisplayed(self):
        return self.driver.find_element(By.XPATH, self.lblFollowingListLoader).is_displayed()

    def getFollowingList(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.lblFollowingList)))
        for user in self.driver.find_elements(By.XPATH, self.lblFollowingList):
            print(user.text)
            self.lstFollowing.append(user.text)
        print(self.lstFollowing)

    def getFollowersList(self):
        time.sleep(2)
        for user in self.driver.find_elements(By.XPATH, self.lblFollowersList):
            print(user.text)
            self.lstFollowers.append(user.text)

    def getIGMembersWhoFollowYouBack(self):
        print("--------Good people. These users are following you back---------")
        for val1 in self.lstFollowing:
            for val2 in self.lstFollowers:
                if val1 == val2:
                    print(val1)
        print("--End of good people---")

    def getIGMembersWhoDontFollowYouBack(self):
        print("--------These people does not follow you back---------")
        for val1 in self.lstFollowers:
            for val2 in self.lstFollowing:
                if val1 == val2:
                    self.lstFollowing.remove(val2)

        for val2 in self.lstFollowing:
            print(val2)
        print("-----------End of bad people--------")

    def setExceptList(self, userids):
        # pass
        for temp in userids:
            self.lstExcept.append(temp)
        print("--------Except these from unfollowing---------")
        # print(userids)
        for exceptVal in self.lstExcept:
            for followingVal in self.lstFollowing:
                if exceptVal == followingVal:
                    print(followingVal)
                    self.lstFollowing.remove(followingVal)

    def getTheListToUnfollow(self):
        print("--------These people will be unfollowed------------")
        for val in self.lstFollowing:
            print(val)

    def clickOnUnfollowButton(self):
        self.driver.find_element(By.XPATH, self.btnUnfollow).click()

    def unfollowUsersExceptSelectedUsers(self):
        print(self.lstFollowing)
        for val3 in self.lstFollowing:
            self.navigate_to_account_by_url(val3)
            self.clickOnUnfollowButton()
            self.driver.find_element(By.XPATH, self.btnUnfollowInPopup).click()

    def isFollowButtonDisplayed(self):
        return self.driver.find_element(By.XPATH, self.btnFollow).is_displayed()
