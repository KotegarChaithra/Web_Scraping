from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)

#to take screenshot of full_page
driver.save_screenshot("C:/Users/hp/Documents/Github/Web_Scraping/full_page.png")
time.sleep(2)

#how to take screen shot of particular element
driver.find_element(By.XPATH,"""/html/body/div/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[3]/span/img""").screenshot("C:/Users/hp/Documents/Github/Web_Scraping/girl.png")