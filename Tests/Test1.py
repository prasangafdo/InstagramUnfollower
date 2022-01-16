import softest

from Function.Landing import *
from Function.Login import *


class InstagramAutomator(softest.TestCase):
    def test_getFollowersAndFollowingCount(self):
        Login.loadLoginPage()
        Login.loginToInstagram("username", "password")
        self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Landing.navigateToProfile()
        Landing.getFollowingCount()
        Landing.getFollowersCount()
        Landing.endSession()
        self.assert_all()

