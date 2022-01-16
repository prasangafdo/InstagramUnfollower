from Page.LandingPage import *


class Landing:
    # def loginToInstagram(username, password):
    #     LoginPage.login(username, password)


    @staticmethod
    def isSearchBarDisplayed():
        landingPage = LandingPage()
        return landingPage.isSearchBarDisplayed()

    @staticmethod
    def endSession():
        landingPage = LandingPage()
        landingPage.endSession()

    @staticmethod
    def navigateToProfile():
        landingPage = LandingPage()
        landingPage.navigateToProfile()

    @staticmethod
    def getFollowingCount():
        landingPage = LandingPage()
        # return landingPage.getFollowingCount()
        landingPage.getFollowingCount()

    @staticmethod
    def getFollowersCount():
        landingPage = LandingPage()
        landingPage.getFollowersCount()

