import self as self

from Page.LoginPage import *


class Login:

    # def loginToInstagram(username, password):
    #     LoginPage.login(username, password)
    loginPage = LoginPage()

    @staticmethod
    def loadLoginPage():
        loginPage = LoginPage()
        loginPage.loadLoginPage()

    @staticmethod
    def loginToInstagram(username, password):
        loginPage = LoginPage()
        loginPage.login(username, password)
