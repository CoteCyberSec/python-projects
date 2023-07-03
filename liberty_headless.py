from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import time
import os

###########################################################



#enter the link to the the website you want to automate login.
website_link= "https://myaccount.libertyenergyandwater.com/portal/#/login?LUMA"

#enter your login username
print('Enter your email:')
username = input()

#enter your login password
print('Enter your password:')
password = input()


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


op = webdriver.ChromeOptions()	#uncomment this line,for chrome users
op.add_argument('headless')
browser = webdriver.Chrome(options=op)
browser.get(website_link)
delay = 10
try:
    ue = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, element_for_username)))
    ue.send_keys(username)
    pe = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, element_for_password)))
    pe.send_keys(password)    
    se = browser.find_element(By.XPATH, element_for_submit)
    time.sleep(3)
    se.click()
    
    today = date.today()
    time.sleep(5)
    browser.save_screenshot('liberty_balance_' + str(today) + '.png')
finally:  
    browser.quit()

   
