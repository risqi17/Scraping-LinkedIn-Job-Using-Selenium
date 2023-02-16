import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Driver's path
path = 'chromedriver.exe'
driver = webdriver.Chrome(path)

# Maximize Window
driver.maximize_window() 
driver.minimize_window() 
driver.maximize_window() 
driver.switch_to.window(driver.current_window_handle)
driver.implicitly_wait(1000)

# Enter to the site
driver.get('https://www.linkedin.com/login');
time.sleep(2)

# Accept cookies
driver.find_element_by_xpath("/html/body/div/main/div[1]/div/section/div/div[2]/button[2]").click()

# User Credentials
# Reading txt file where we have our user credentials
with open('user_credentials.txt', 'r',encoding="utf-8") as file:
    user_credentials = file.readlines()
    user_credentials = [line.rstrip() for line in user_credentials]
user_name = user_credentials[0] # First line
password = user_credentials[1] # Second line
driver.find_element_by_xpath('//[@id="username"]').send_keys(user_name)
driver.find_element_by_xpath('//[@id="password"]').send_keys(password)
time.sleep(1)

# Login button
driver.find_element_by_xpath('//*[@id=”organic-div”]/form/div[3]/button').click()
driver.implicitly_wait(30)
