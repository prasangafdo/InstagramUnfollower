import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome("C:/Users/Prasanga Fernando/Downloads/chromedriver_win32/chromedriver.exe")
# Old way of fixing the issue

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")

driver.find_element(By.NAME, "q").send_keys("Instagram")
driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@value='Google Search']").click()
time.sleep(4)

