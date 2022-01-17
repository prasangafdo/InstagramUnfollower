import time

from selenium.webdriver import ActionChains, Keys

from Page.LoginPage import *


class AccountPage(LoginPage):

    lblFollowingCount = "//a[contains(@href,'following')]/span"
    lblFollowersCount = "//a[contains(@href,'followers')]/span"
    lstFollowing = "//div[@class='isgrP']"
    lblFollowingListLoader = "//li[@class='wo9IH QN7kB ']/div/*[name()='svg']"
    lnkFollowing = "//a[contains(@href,'following')]"
    lblFollowingPopUp = "//div[@aria-label='Following']"

    # mmm = "//a[@href='/ruu_1111/']"
    # mmm = "(//div[@class='PZuss']/li)[1]"
    mmm = "//div[@class='isgrP']"

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

    def scrollDownFollowingList(self):
        time.sleep(7)
        actions = ActionChains(LoginPage.driver)
        actions.move_to_element(LoginPage.driver.find_element(By.XPATH, self.mmm))
        # perform the operation on the element
        # actions.click((LoginPage.driver.find_element(By.XPATH, self.mmm)))
        actions.perform()
        time.sleep(1)
        # LoginPage.driver.find_element(By.XPATH, self.lstFollowing).send_keys(Keys.PAGE_DOWN)
        # LoginPage.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # html = LoginPage.driver.find_element(By.XPATH, self.lblFollowingPopUp)
        LoginPage.driver.find_element(By.XPATH, self.mmm).send_keys(Keys.END)
        # actions.perform()
        time.sleep(3)
