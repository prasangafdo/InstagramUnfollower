from Page.LandingPage import *


    # def loginToInstagram(username, password):
    #     LoginPage.login(username, password)

def isSearchBarDisplayed():
    landingPage = LandingPage()
    return landingPage.isSearchBarDisplayed()

def endSession():
    landingPage = LandingPage()
    landingPage.endSession()

def navigateToProfile():
    landingPage = LandingPage()
    landingPage.navigateToProfile()
