import logging
import sys
import pytest
import softest

# sys.path.append("..")
# from Function import Login, Account
from Function import Landing
from Function import Account, Login, Message
from Constants import Credentials


# from Page import MessagesPage

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

    def test_get_followers_and_following_count(self):
        Login.loadLoginPage()
        # Login.loginToMobileView("username", "password")
        Account.navigateToAccountByURL("prasangafdz")
        Account.getFollowersCount()
        Account.getFollowingCount()
        Landing.endSession()
        self.assert_all()

    def test_getFollowersList(self):
        Login.loadLoginPage()
        Login.loginToMobileView(Credentials.Username, Credentials.Password)
        # self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Account.navigateToAccountByURL("prasangafdz")
        Account.clickOnFollowersLink()
        Account.scrollDownTheList()
        # Account.getFollowersList()
        Account.getFollowingList()
        Landing.endSession()
        self.assert_all()

    def test_getIGMembersWhoFollowYouBack(self):
        # a = ["panda", "milo", "baby", "baba"]
        # b = ["panda", "baby", "nanny", "pinky"]
        #
        # for val1 in a:
        #     for val2 in b:
        #         if val1 == val2:
        #             print(val1)
        Login.loadLoginPage()
        Login.loginToMobileView(Credentials.Username, Credentials.Password)
        # self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Account.navigateToAccountByURL("prasangafdz")
        Account.clickOnFollowersLink()
        Account.scrollDownTheList()
        Account.getFollowersList()
        Account.navigateToAccountByURL("prasangafdz")
        Account.clickOnFollowingLink()
        Account.scrollDownTheList()
        # Account.getFollowersList()
        Account.getFollowingList()
        Account.getIGMembersWhoFollowYouBack()

    def test_getIGMembersWhoDontFollowYouBack(self):
        Login.loadLoginPage()
        Login.loginToMobileView(Credentials.Username, Credentials.Password)
        # self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Account.navigateToAccountByURL("prasangafdz")
        Account.clickOnFollowersLink()
        Account.scrollDownTheList()
        Account.getFollowersList()
        Account.navigateToAccountByURL("prasangafdz")
        Account.clickOnFollowingLink()
        Account.scrollDownTheList()
        # Account.getFollowersList()
        Account.getFollowingList()
        Account.getIGMembersWhoDontFollowYouBack()

    def test_unfollowIGMembersWhoDontFollowYouBack(self):
        Login.loadLoginPage()
        Login.loginToMobileView(Credentials.Username, Credentials.Password)
        # self.soft_assert(self.assertTrue, Landing.isSearchBarDisplayed())
        Account.navigateToAccountByURL(Credentials.accountName)
        Account.clickOnFollowersLink()
        Account.scrollDownTheList()
        Account.getFollowersList()
        Account.navigateToAccountByURL(Credentials.accountName)
        Account.clickOnFollowingLink()
        Account.scrollDownTheList()
        # Account.getFollowersList()
        Account.getFollowingList()
        Account.getIGMembersWhoDontFollowYouBack()

    #         Not completed yet

    def test_unfollowIGMembersWhoDontFollowYouBackExceptForSelectedMembers(self):
        # Sometimes we don't need to unfollow everyone.
        # In such scenarios set excepted list with userids and run this script
        Login.loadLoginPage()
        Login.loginToMobileView(Credentials.Username, Credentials.Password)
        Account.navigateToAccountByURL(Credentials.accountName)
        Account.clickOnFollowersLink()
        Account.scrollDownTheList()
        Account.getFollowersList()
        Account.navigateToAccountByURL(Credentials.accountName)
        Account.clickOnFollowingLink()
        Account.scrollDownTheList()
        # Account.getFollowersList()
        Account.getFollowingList()
        Account.getIGMembersWhoDontFollowYouBack()
        lstUsers = ["sanu_life, naguleskrrish, explorers.lk"]
        # Pass the excepted user ids here
        Account.setexceptedUserList(lstUsers)
        Account.getTheListToUnfollow()
        Account.unfollowUsersExceptSelectedUsers()
        Landing.endSession()

    def test_deleteAllSentMessagesToAParticularUser(self):
        Login.loadLoginPage()
        Login.loginToMobileView(Credentials.Username, Credentials.Password)
        Account.navigateToAccountByURL(Credentials.accountName)
        Landing.navigateToHome()
        Landing.clickCancelFromAddToHomePopup()
        Landing.openDirectMessages()
        Landing.clickNotNowFromEnableNotificationPopup()
        Message.openMessageRequests()
        Message.openUserThread()
        # Message.scrollToTop()
        Message.scrollUp()
        Message.deleteMessage()

        # Scroll to top
        # window.scrollTo(0, 0);
        # window.scrollTo({ top: 0, behavior: 'smooth' });
