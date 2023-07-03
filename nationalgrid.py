from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

###########################################################



#enter the link totp the website you want to automate login.
website_link= "https://login.nationalgridus.com/loginnationalgridus.onmicrosoft.com/oauth2/v2.0/authorize?cancel_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauth%2Fsso%2FNGP_SignIn_NY_Upstate_Home&client_id=88d004b4-3d39-4599-b410-093849907ee5&customer_type=home&p=B2C_1A_UWP_NationalGrid_convert_merge_signin&redirect_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauthcallback%2FNGP_SignIn_NY_Upstate_Home&region=nyupstate&response_type=code&scope=https%3A%2F%2Flogin.nationalgridus.com%2Fapi%2Fread+openid+profile+email+offline_access&state=CAAAAYkcIK9xMDAwMDAwMDAwMDAwMDAwAAAA9IpwKlF8e-U2ghN2CWQVP8zszblXj-tw-wafPDzu00PH5BpCy9WyIZXSVDm48Vc285d3LR0r-87wtLKOG5WXmH_PUm0OOuyPUMuUm6x_Om2gW0Pd5LmjyCVVqAkOVocvz4qMTAQJnMF-am44ivdOygmFIeh1D2mx9ks4TncNUZODVisLhFlt-0bpbKfokbNZsMnOhT35lUxc5ycLtT7vm7BOoBBAhbZ-7uxZ0wxqyYaa&switch_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fs%2Flogin"
#enter your login username
print('Enter your email:')
username=input()
#enter your login password
print('Enter your password:')
password=input()

continuebuttonelement='//*[@id="modal-content-id-1-7"]/div/a'

###########################################################

#enter the element for username input field
element_for_username='//*[@id="signInName"]'
#enter the element for password input field
element_for_password='//*[@id="password"]'
#enter the element for submit button
element_for_submit="interceptButton"

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
signInButton = browser.find_element(By.ID, element_for_submit)
signInButton.click()


time.sleep(5)
continuebutton = browser.find_element(By.XPATH, continuebuttonelement)
time.sleep(5)
continuebutton.click()
time.sleep(60)
browser.quit()

	

