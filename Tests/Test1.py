import softest

from Function.Landing import *
from Function.Login import *


class InstagramAutomator(softest.TestCase):
    def getFollowersList(self):
        Login.loadLoginPage()
        Login.loginToInstagram("username", "password")
    #     self.soft_assert(self.assertTrue(Landing.isSearchBarDisplayed()))
    #
    # getFollowersList(self)
