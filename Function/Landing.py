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

def openDirectMessages():
    landingPage = LandingPage()
    landingPage.openDirectMessages()

def navigateToHome():
    landingPage = LandingPage()
    landingPage.navigateToHome()

def clickCancelFromAddToHomePopup():
    landingPage = LandingPage()
    landingPage.clickCancelFromAddToHomePopup()

def clickNotNowFromEnableNotificationPopup():
    landingPage = LandingPage()
    landingPage.clickNotNowFromEnableNotificationPopup()

