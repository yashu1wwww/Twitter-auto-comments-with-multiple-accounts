#upto 5 accounts you can auto tweet for more add more twitter 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Twitter accounts (Replace with valid credentials)
accounts = [
    {"username": "account1", "password": "password1"},
    {"username": "account2", "password": "password2"},
    {"username": "account3", "password": "password3"},
    {"username": "account4", "password": "password4"},
    {"username": "account5", "password": "password5"}
]

# List of possible comments
commentsDict = [
    'good', 'amazing one', 'keep going', 'excellent', 'next video please', 'sub to your channel',
    'shared to others', 'made my day', 'keep it up', 'sensational', 'rock it', 'challenge it',
    'post video daily', 'work was amazing', 'needed more edit', 'edit was awesome', 'what a video man',
    'watched yesterday', 'you are genius', 'faster than light', 'your work needed success', 'new fan of you',
    'keep rocking dude', 'copy cat', 'link the video', 'listening', 'writing', 'reading', 'playing'
]

# Target tweet URL (Replace with the actual tweet link)
tweet_url = "https://twitter.com/elonmusk/status/1708660084992029126"

# Number of comments per account
MAX_COMMENTS = 5  

# Function to login, comment, and logout
def twitter_comment(account):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(4)

    try:
        # Enter username
        email = driver.find_element(By.NAME, 'text')
        email.send_keys(account["username"])
        email.send_keys(Keys.ENTER)
        time.sleep(3)

        # Enter password
        password = driver.find_element(By.NAME, "password")
        password.send_keys(account["password"])
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # Navigate to the tweet
        driver.get(tweet_url)
        time.sleep(5)

        # Comment loop
        for _ in range(MAX_COMMENTS):
            try:
                # Select a random comment
                comment = random.choice(commentsDict)

                # Find the comment box and type the comment
                send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
                send_button.send_keys(comment)
                time.sleep(1)

                # Click the reply button
                driver.execute_script('document.querySelector("[data-testid=\'tweetButtonInline\']").click()')
                time.sleep(2)

            except Exception as e:
                print(f"Error posting comment: {e}")
                break

    except Exception as e:
        print(f"Error logging in for {account['username']}: {e}")

    # Close browser before moving to next account
    time.sleep(2)
    driver.quit()

# Loop through all accounts
for acc in accounts:
    twitter_comment(acc)
    time.sleep(5)  # Pause between account switches
