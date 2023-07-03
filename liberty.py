from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date



import time
import os

###########################################################



#enter the link totp the website you want to automate login.
website_link= "https://myaccount.libertyenergyandwater.com/portal/#/login?LUMA"
#enter your login username

username='ENTER USERNAME HERE'
#enter your login password

password='ENTER PASSWORD HERE'


###########################################################

#enter the element for username input field
element_for_username='//*[@id="username"]'
#enter the element for password input field
element_for_password='//*[@id="password"]'
#enter the element for submit button
element_for_submit="/html/body/div/div/div[2]/section/div/div/div[3]/div/form/div[4]/button"

###########################################################

#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
#browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
browser = webdriver.Chrome()	#uncomment this line,for chrome users
browser.get((website_link))	


username_element = browser.find_element(By.XPATH, element_for_username)
username_element.send_keys(username)
time.sleep(1)
password_element  = browser.find_element(By.XPATH, element_for_password)
password_element.send_keys(password)
time.sleep(1)
signInButton = browser.find_element(By.XPATH, element_for_submit)
signInButton.click()
time.sleep(5)

today = date.today()

browser.save_screenshot('balance_' + str(today) + '.png')
time.sleep(60)



browser.quit()
