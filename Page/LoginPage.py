import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 740, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

    options = Options()
    # options.add_argument("start-maximized")
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    # options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Desktop view buttons
    lblUsername = "//input[contains(@aria-label, 'Phone number')]"
    lblPassword = "//input[contains(@aria-label, 'Password')]"
    btnLogin = "//div[text()='Log In']/parent::button"

    # Mobile view buttons
    btnInitialLogin = "//button[text()='Log In']"

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

    def loginToMobileView(self, username, password):
        time.sleep(6)
        self.driver.find_element(By.XPATH, self.btnInitialLogin).click()
        self.driver.find_element(By.XPATH, self.lblUsername).send_keys(username)
        # self.driver.find_element(self.lblPassword).click()
        self.driver.find_element(By.XPATH, self.lblPassword).send_keys(password)
        self.driver.find_element(By.XPATH, self.btnLogin).click()
        time.sleep(5)

#
# login = LoginPage()
# login.loadLoginPage()
# def loadLoginPage():
#     LoginPage.loadLoginPage()
