from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words for comments to tweet

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(7)
email = driver.find_element_by_name('text')
email.send_keys("twitter123") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("Tweet123@#$%") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://twitter.com/X/status/1705276556334031256")  #replace with your url where you  wanted to auto cmts to that post 
time.sleep(7)

counter = 0
while True:
    try:
        
        # comment the word
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(random.choice(commentsDict))
        
        time.sleep(1)
        
        # Click the send button
        click_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span/span')
        click_button.click()
        
        time.sleep(2)  

        counter += 1
        if counter == 5: #change how much you want comments to the tweet per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)

driver.close()

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(7)
email = driver.find_element_by_name('text')
email.send_keys("twitter234") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twitter123@#$%") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://twitter.com/DbossD56/status/1705557604209226080")  #replace with your url where you  wanted to auto cmts to that post 
time.sleep(7)

counter = 0
while True:
    try:
        
        # comment the word
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(random.choice(commentsDict))
        
        time.sleep(1)
        
        # Click the send button
        click_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/span/span')
        click_button.click()
        
        time.sleep(2)  

        counter += 1
        if counter == 5: #change how much you want comments to the tweet per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)

driver.close()





