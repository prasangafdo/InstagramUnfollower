from Page.AccountPage import *

# def loginToInstagram(username, password):
#     LoginPage.login(username, password)

def getFollowingCount():
    accountPage = AccountPage()
    # return landingPage.getFollowingCount()
    accountPage.getFollowingCount()

def getFollowersCount():
    accountPage = AccountPage()
    accountPage.getFollowersCount()


def clickOnFollowingLink():
    accountPage = AccountPage()
    accountPage.clickOnFollowingLink()




def scrollDownFollowingList():
    accountPage = AccountPage()
    accountPage.scrollDownFollowingList()
