from Page.LoginPage import *


def loadLoginPage():
    loginPage = LoginPage()
    loginPage.loadLoginPage()


def loginToInstagram(username, password):
    loginPage = LoginPage()
    loginPage.login(username, password)

def loginToMobileView(username, password):
    loginPage = LoginPage()
    loginPage.loginToMobileView(username, password)