# Step 3.2

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

# Select language
language_xpath = "//*[@id='langSelect-EN']"
wait = WebDriverWait(driver, 10)
language_element = wait.until(EC.presence_of_element_located((By.XPATH, language_xpath)))
language_element.click()
time.sleep(3)

# Cookie Xpath
cookie_xpath = "//*[@id='bigCookie']"
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, cookie_xpath)))

# Click on cookie
count = 0
count_xpath = "//*[@id='cookies']"
while int(count) < 100:
	# Define cookie element in the loop to avoid stale element
	cookie_element = driver.find_element(By.XPATH, cookie_xpath)
	cookie_element.click()
	# Get cookie counter
	count = driver.find_element(By.XPATH, count_xpath).text.split(' ')[0]

time.sleep(10)
driver.quit()