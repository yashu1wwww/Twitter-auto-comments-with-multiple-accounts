#upto 5 accounts 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

# List of comments to post
commentsDict = [
    'good', 'amazing one', 'keep going', 'excellent', 'next video please', 'sub to your channel',
    'shared to others', 'made my day', 'keep it up', 'sensational', 'rock it', 'challenge it',
    'post video daily', 'work was amazing', 'needed more edit', 'edit was awesome', 'what a video man',
    'watched yesterday', 'you are genius', 'faster than light', 'your work needed success', 'new fan of you',
    'keep rocking dude', 'copy cat', 'link the video', 'listening', 'writing', 'reading', 'playing'
]  # Replace with your words

# Set the number of comments you want to post
MAX_COMMENTS = 1 

driver = webdriver.Chrome()
driver.maximize_window()

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
time.sleep(4)

# Enter username
email = driver.find_element(By.NAME, 'text')
email.send_keys("twitter123")  # Replace with your valid Twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("twitter_1234")  # Replace with your valid Twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)

# Navigate to the target tweet
driver.get("https://twitter.com/elonmusk/status/1708660084992029126")  # Replace with your tweet URL
time.sleep(5)

# Counter to track the number of comments posted
counter = 0

for comment in commentsDict:
    try:
        # Find the comment input box and type the comment
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(comment)
        time.sleep(1)
        
        # Click the post reply button
        driver.execute_script('document.querySelector("[data-testid=\'tweetButtonInline\']").click()')
        time.sleep(2)

        counter += 1
        if counter == MAX_COMMENTS:  # Stop when reaching the desired number of comments
            break

    except Exception as e:
        print("An error occurred:", e)
        break

# Close the browser
time.sleep(2)
driver.close()


#2nd account
driver = webdriver.Chrome()
driver.maximize_window()

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
time.sleep(4)

# Enter username
email = driver.find_element(By.NAME, 'text')
email.send_keys("twitter123")  # Replace with your valid Twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("twitter_1234")  # Replace with your valid Twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)

# Navigate to the target tweet
driver.get("https://twitter.com/elonmusk/status/1708660084992029126")  # Replace with your tweet URL
time.sleep(5)

# Counter to track the number of comments posted
counter = 0

for comment in commentsDict:
    try:
        # Find the comment input box and type the comment
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(comment)
        time.sleep(1)
        
        # Click the post reply button
        driver.execute_script('document.querySelector("[data-testid=\'tweetButtonInline\']").click()')
        time.sleep(2)

        counter += 1
        if counter == MAX_COMMENTS:  # Stop when reaching the desired number of comments
            break

    except Exception as e:
        print("An error occurred:", e)
        break

# Close the browser
time.sleep(2)
driver.close()

#3rd account
driver = webdriver.Chrome()
driver.maximize_window()

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
time.sleep(4)

# Enter username
email = driver.find_element(By.NAME, 'text')
email.send_keys("twitter123")  # Replace with your valid Twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("twitter_1234")  # Replace with your valid Twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)

# Navigate to the target tweet
driver.get("https://twitter.com/elonmusk/status/1708660084992029126")  # Replace with your tweet URL
time.sleep(5)

# Counter to track the number of comments posted
counter = 0

for comment in commentsDict:
    try:
        # Find the comment input box and type the comment
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(comment)
        time.sleep(1)
        
        # Click the post reply button
        driver.execute_script('document.querySelector("[data-testid=\'tweetButtonInline\']").click()')
        time.sleep(2)

        counter += 1
        if counter == MAX_COMMENTS:  # Stop when reaching the desired number of comments
            break

    except Exception as e:
        print("An error occurred:", e)
        break

# Close the browser
time.sleep(2)
driver.close()

#4th account
driver = webdriver.Chrome()
driver.maximize_window()

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
time.sleep(4)

# Enter username
email = driver.find_element(By.NAME, 'text')
email.send_keys("twitter123")  # Replace with your valid Twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("twitter_1234")  # Replace with your valid Twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)

# Navigate to the target tweet
driver.get("https://twitter.com/elonmusk/status/1708660084992029126")  # Replace with your tweet URL
time.sleep(5)

# Counter to track the number of comments posted
counter = 0

for comment in commentsDict:
    try:
        # Find the comment input box and type the comment
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(comment)
        time.sleep(1)
        
        # Click the post reply button
        driver.execute_script('document.querySelector("[data-testid=\'tweetButtonInline\']").click()')
        time.sleep(2)

        counter += 1
        if counter == MAX_COMMENTS:  # Stop when reaching the desired number of comments
            break

    except Exception as e:
        print("An error occurred:", e)
        break

# Close the browser
time.sleep(2)
driver.close()

#5th account
driver = webdriver.Chrome()
driver.maximize_window()

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
time.sleep(4)

# Enter username
email = driver.find_element(By.NAME, 'text')
email.send_keys("twitter123")  # Replace with your valid Twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("twitter_1234")  # Replace with your valid Twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)

# Navigate to the target tweet
driver.get("https://twitter.com/elonmusk/status/1708660084992029126")  # Replace with your tweet URL
time.sleep(5)

# Counter to track the number of comments posted
counter = 0

for comment in commentsDict:
    try:
        # Find the comment input box and type the comment
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        send_button.send_keys(comment)
        time.sleep(1)
        
        # Click the post reply button
        driver.execute_script('document.querySelector("[data-testid=\'tweetButtonInline\']").click()')
        time.sleep(2)

        counter += 1
        if counter == MAX_COMMENTS:  # Stop when reaching the desired number of comments
            break

    except Exception as e:
        print("An error occurred:", e)
        break

# Close the browser
time.sleep(2)
driver.close()



