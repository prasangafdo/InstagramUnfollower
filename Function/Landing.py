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
