from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://x.com/home")

element = WebDriverWait(driver,10).until(ec.presence_of_element_located(By.XPATH))

#1st method
# time.sleep(4)
# login=driver.find_element(By.XPATH,"""/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div""").click()

# input_email = driver.find_element(By.XPATH,"""/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input""")
# input_email.send_keys("chaithrakotegar8197@gmail.com")

# next = driver.find_element(By.XPATH,"""/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]""").click()

search = driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input""")
search.send_keys("elon_musk")
search.send_keys(Keys.ENTER)

#2nd method

