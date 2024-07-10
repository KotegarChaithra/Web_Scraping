from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://www.wscubetech.com/")
driver.find_element_by_xpath("""/html/body/section[4]/div/div/div[3]/div""")# path expression which gives path of any element

driver.find_element_by_xpath("""/html/body/section[1]/div[2]/div/div[1]/div[2]/div/button""")