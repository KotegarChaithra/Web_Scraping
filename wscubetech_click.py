from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://x.com/?lang=en")
time.sleep(2)

driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/a/div/span/span""").click()
time.sleep(1)

name = driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/label/div/div[2]/div/input""")
name.send_keys("superselenium")

mobile = driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/label/div/div[2]/div/input""")
mobile.send_keys("1234567890")

month_search = driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div/div[1]/select""")
month_search.send_keys("september")
month_search.send_keys(Keys.ENTER)

day_search = driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div/div[2]/select""")
day_search.send_keys("21")
day_search.send_keys(Keys.ENTER)

year_search = driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div/div[3]/select""")
year_search.send_keys("1999")
year_search.send_keys(Keys.ENTER)

next = driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/button/div""").click()