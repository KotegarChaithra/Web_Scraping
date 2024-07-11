from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://www.google.com/")
time.sleep(2)

search = driver.find_element(By.XPATH,"""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys("wscubetech")
search.send_keys(Keys.ENTER)
