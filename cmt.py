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

commentsDict = ['good @elonmusk', 'amazing one @elonmusk']  # Tambahkan komentar sesuai kebutuhan
comment_iterator = iter(commentsDict) #replace with your words for comments to tweet

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
driver.get("https://twitter.com/elonmusk/status/1708660084992029126")  #replace with your url where you  wanted to auto cmts to that post 
time.sleep(5)

counter = 0
    try:
    while True:
        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweet']/div").click()  # retweet button
        time.sleep(1) #retweet button

        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweetConfirm']/div").click()  # retweet click #confirm
        time.sleep(2) #click on retweet button

        like_button = driver.find_element_by_xpath("//div[@data-testid='like']/div")  # like button
        like_button.click() #click on like button
        
        time.sleep(2)
        
        comment = next(comment_iterator)
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(comment)
except StopIteration:
    print("All comments have been used.")
        
        time.sleep(1)
        
        # Click the post reply
        driver.execute_script('document.querySelector("#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > section > div > div > div:nth-child(2) > div > div > div > div > div.css-175oi2r.r-14lw9ot.r-1h8ys4a.r-1f1sjgu > div:nth-child(2) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-14lw9ot.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19u6a5r.r-2yi16.r-1qi8awa.r-ymttw5.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l").click()')
        
        time.sleep(2)  

        counter += 1
        if counter == 1: #Change '5' to 'how many comments you want to do for a post...
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
driver.get("https://twitter.com/elonmusk/status/1708660084992029126")  #replace with your url where you  wanted to auto cmts to that post 
time.sleep(7)

counter = 0
try:
    while True:
        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweet']/div").click()  # retweet button
        time.sleep(1) #retweet button

        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweetConfirm']/div").click()  # retweet click #confirm
        time.sleep(2) #click on retweet button

        like_button = driver.find_element_by_xpath("//div[@data-testid='like']/div")  # like button
        like_button.click() #click on like button
        
        time.sleep(2)
        
        comment = next(comment_iterator)
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(comment)
except StopIteration:
    print("All comments have been used.")
        
        time.sleep(1)
        
        # Click the post reply
        driver.execute_script('document.querySelector("#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > section > div > div > div:nth-child(2) > div > div > div > div > div.css-175oi2r.r-14lw9ot.r-1h8ys4a.r-1f1sjgu > div:nth-child(2) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-14lw9ot.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19u6a5r.r-2yi16.r-1qi8awa.r-ymttw5.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l").click()')
        
        time.sleep(2)  

        counter += 1
        if counter == 1: #Change '5' to 'how many comments you want to do for a post...
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)

driver.close()





