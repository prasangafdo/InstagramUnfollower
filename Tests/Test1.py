import logging
import sys

import softest

sys.path.append("..")
from Function import Login
from Function import Landing

# from ..Function import Landing
# import Function


class InstagramAutomator(softest.TestCase):
    def test_LoginWithValidCredentials(self):
        Login.loadLoginPage()
        Login.loginToInstagram("prasangafdz", "Devil18@#")
        self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Landing.navigateToProfile()
        Landing.endSession()
        self.assert_all()

    def test_getFollowersAndFollowingCount(self):
        Login.loadLoginPage()
        Login.loginToInstagram("username", "password")
        self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Landing.navigateToProfile()
        Landing.getFollowingCount()
        Landing.getFollowersCount()
        Landing.endSession()
        self.assert_all()

    def test_getFollowingsList(self):
        Login.loadLoginPage()
        Login.loginToInstagram("username", "password")
        self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Landing.navigateToProfile()

        Landing.endSession()
        self.assert_all()
