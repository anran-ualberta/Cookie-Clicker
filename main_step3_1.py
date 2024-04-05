# Step 3.1

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

language_xpath = "//*[@id='langSelect-EN']"
# Wait for a element to appear before proceeding further in the code
wait = WebDriverWait(driver, 10)
language_element = wait.until(EC.presence_of_element_located((By.XPATH, language_xpath)))
# Click on English
language_element.click()

time.sleep(10)
driver.quit()