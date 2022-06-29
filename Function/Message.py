from Page.MessagesPage import *


    # def loginToInstagram(username, password):
    #     LoginPage.login(username, password)

def openMessageRequests():
    messages = MessagesPage()
    messages.openMessageRequests()

def scrollToTop():
    messages = MessagesPage()
    messages.scrollToTop()

def openUserThread():
    messages = MessagesPage()
    messages.openUserThread()

def deleteMessage():
    messages = MessagesPage()
    messages.touchAndHoldAmessage()

def scrollUp():
    messages = MessagesPage()
    messages.scrollUp()


