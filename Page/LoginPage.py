import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    options = Options()
    # options.add_argument("start-maximized")
    options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    lblUsername = "//input[contains(@aria-label, 'Phone number')]"
    lblPassword = "//input[contains(@aria-label, 'Password')]"
    btnLogin = "//div[text()='Log In']/parent::button"

    def loadLoginPage(self):
        self.driver.set_page_load_timeout(10)
        self.driver.get("https://www.instagram.com/")

    def login(self, username, password):
        time.sleep(4)
        # self.driver.find_element(self.lblUsername).click()
        self.driver.find_element(By.XPATH, self.lblUsername).send_keys(username)
        # self.driver.find_element(self.lblPassword).click()
        self.driver.find_element(By.XPATH, self.lblPassword).send_keys(password)
        self.driver.find_element(By.XPATH, self.btnLogin).click()
#
# login = LoginPage()
# login.loadLoginPage()
# def loadLoginPage():
#     LoginPage.loadLoginPage()
