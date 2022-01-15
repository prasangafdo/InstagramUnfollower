import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.headless = True

options = Options()
# options.add_argument("start-maximized")
options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# driver = webdriver.Chrome("C:/Users/Prasanga Fernando/Downloads/chromedriver_win32/chromedriver.exe")
# Old way of fixing the issue

driver.set_page_load_timeout(10)
driver.get("https://www.instagram.com/")

#
# driver.find_element(By.NAME, "q").send_keys("Instagram")
# driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@value='Google Search']").click()

time.sleep(4)
