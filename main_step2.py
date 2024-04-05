# Step 2

# Import the WebDriver and By class (for locating elements)
from selenium import webdriver
from selenium.webdriver.common.by import By

# Add a "pause" time to make the browser visible
import time

# Launch browser in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Use driver.get method to navigate to a given URL
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)

# Close the browser once done
driver.quit()