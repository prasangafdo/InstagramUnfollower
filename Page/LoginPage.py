import By as By


class LoginPage:
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    # options.add_argument("start-maximized")
    options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    lblUsername = By.XPATH, "//input[contains(@aria-label, 'Phone number')]"
    lblPassword = By.XPATH, "//input[contains(@aria-label, 'Password')]"

    def login(self, username, password):
        self.driver.find_element(self.lblUsername).send_keys(username)
        self.driver.find_element(self.lblPassword).send_keys(password)

