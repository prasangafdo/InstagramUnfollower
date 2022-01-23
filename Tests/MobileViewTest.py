import logging
import sys

import softest

# sys.path.append("..")
# from Function import Login, Account
from Function import Landing
from Function import  Account,Login


# from ..Function import Landing
# import Function


class InstagramAutomator(softest.TestCase):
    # def test_LoginWithValidCredentials(self): # These codes are not configured for mobile view yet
    #     Login.loadLoginPage()
    #     Login.loginToInstagram("username", "password")
    #     self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
    #     Landing.navigateToProfile()
    #     Landing.endSession()
    #     self.assert_all()

    def test_getFollowersAndFollowingCount(self):
        Login.loadLoginPage()
        # Login.loginToMobileView("username", "password")
        Account.navigateToAccountByURL("prasangafdz")
        Account.getFollowersCount()
        Account.getFollowingCount()
        Landing.endSession()
        self.assert_all()

    def test_getFollowingsList(self):
        Login.loadLoginPage()
        Login.loginToMobileView("username", "password")
        # self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Account.navigateToAccountByURL("prasangafdz")
        Account.clickOnFollowersLink()
        Account.scrollDownTheList()
        Account.getFollowersList()
        Account.getFollowingList()
        Landing.endSession()
        self.assert_all()

    def test_getFollowersWhoFollowYouBack(self):
        a = ["panda", "milo", "baby", "baba"]
        b = ["panda", "baby", "nanny", "pinky"]

        for val1 in a:
            for val2 in b:
                if val1 == val2:
                    print(val1)

