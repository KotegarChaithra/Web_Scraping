#How to find XPATH?
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service = s)
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)# gives sometime to load website,wait up to 2 seconds and afetr 2 sec it will click any button

driver.find_element(By.XPATH,"""/html/body/div/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[2]/button""").click()
time.sleep(2)

driver.find_element(By.XPATH,"""/html/body/div/div[2]/div[2]/section/div/div[2]/div[1]/div/ul/li[7]/a""").click()