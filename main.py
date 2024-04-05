import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

# Select language
language_xpath = "//*[@id='langSelect-EN']"
language_element = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.XPATH, language_xpath))
)
language_element.click()
time.sleep(3)

# Click on cookie
count = 0
cookie_xpath = "//*[@id='bigCookie']"
count_xpath = "//*[@id='cookies']"
while int(count) < 100:
	cookie_element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, cookie_xpath))
	)
	cookie_element.click()
	count = driver.find_element(By.XPATH, count_xpath).text.split(' ')[0]
time.sleep(3)

# Grandma upgrade
grandma_xpath = "//*[@id='product1']"
grandma_element = driver.find_element(By.XPATH, grandma_xpath)
grandma_element.click()
time.sleep(3)

# Assert
count = driver.find_element(By.XPATH, count_xpath).text.split(' ')[0]
assert int(count) < 100

time.sleep(10)
driver.quit()