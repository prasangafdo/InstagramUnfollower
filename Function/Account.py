from Page.AccountPage import *

# def loginToInstagram(username, password):
#     LoginPage.login(username, password)
accountPage = AccountPage()


def getFollowingCount():
    accountPage = AccountPage()
    # return landingPage.getFollowingCount()
    accountPage.getFollowingCount()


def getFollowersCount():
    # accountPage = AccountPage()
    accountPage.getFollowersCount()


def clickOnFollowingLink():
    # accountPage = AccountPage()
    accountPage.clickOnFollowingLink()

def clickOnFollowersLink():
    # accountPage = AccountPage()
    accountPage.clickOnFollowersLink()


def scrollDownTheList():
    # accountPage = AccountPage()
    accountPage.scrollDownTheList()


def navigateToAccountByURL(accountID):
    accountPage.navigateToAccountByURL(accountID)


def getFollowingList():
    accountPage.getFollowingList()


def getFollowersList():
    accountPage.getFollowersList()
