#here i am added upto 3 accs which auto login to auto cmts to the post....
#(note for auto login used accs must be non authentication accounts)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(8)
email = driver.find_element_by_name('text')
email.send_keys("xvavava")    #replace with your twitter username        
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("whahaja")      #replace with your twitter pass        
password.send_keys(Keys.ENTER)
time.sleep(7)
driver.get("https://twitter.com/imVkohli/status/1551956168469147648?s=20&t=7L48oKsoQwTBDStoli73jg")   #replace with your url where you  wanted to auto cmts to that post 
time.sleep(8)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("swaag") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("seas") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("sea") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("seeing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing concept") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("tweeting") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("commenting") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("using it") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.close()

#after login and auto cmts its close and open and login to another account and make auto cmts so replace username and pass and url and  cmts(which cmts you want) in below

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(8)
email = driver.find_element_by_name('text')
email.send_keys("@erara")    #replace with your twitter username       
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("ahajaja")    #replace with your twitter pass      
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://twitter.com/imVkohli/status/1551956168469147648?s=20&t=7L48oKsoQwTBDStoli73jg")   #replace with your url where you  wanted to auto cmts to that post 
time.sleep(8)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("swaag") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("seas") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("sea") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("seeing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing concept") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("tweeting") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("commenting") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("using it") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.close()

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(8)
email = driver.find_element_by_name('text')
email.send_keys("secure")            #replace with your twitter username 
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("random")       #replace with your twitter pass
password.send_keys(Keys.ENTER)
time.sleep(7)
driver.get("https://twitter.com/imVkohli/status/1551956168469147648?s=20&t=7L48oKsoQwTBDStoli73jg")   #replace with your url where you  wanted to auto cmts to that post 
time.sleep(8)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("swaag") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("seas") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("sea") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("seeing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing concept") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("tweeting") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("commenting") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("using it") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.find_element_by_class_name('public-DraftStyleDefault-ltr').send_keys("amazing") #replace with your required cmt
comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))).click()
time.sleep(5)
driver.close()

