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

    # def test_getFollowersAndFollowingCount(self):
    #     Login.loadLoginPage()
    #     Login.loginToInstagram("username", "password")
    #     self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
    #     Landing.navigateToProfile()
    #     Account.getFollowersCount()
    #     Account.getFollowersCount()
    #     Landing.endSession()
    #     self.assert_all()

    def test_getFollowingsList(self):
        Login.loadLoginPage()
        Login.loginToInstagram("username", "password")
        # self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Account.navigateToAccountByURL("prasangafdz")
        Account.clickOnFollowingLink()
        Account.scrollDownFollowingList()
        Account.getFollowersList()

        Landing.endSession()
        self.assert_all()
