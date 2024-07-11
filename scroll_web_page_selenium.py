from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/hp/Documents/softwares/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://www.google.com/search?sca_esv=775099f247dfe703&sca_upv=1&sxsrf=ADLYWIKolNV71kfsvVD7wNWbLc_ToDyKaA:1720709773661&q=pandas&udm=2&fbs=AEQNm0B8dVdIWR07uWWlg1TdKnNtA1cwMugrQsIKmAo5AEZHWRFlUeGLxYlhagMfUatSvHu3MSamP9Qd2SfjyZyVIdPFrZFmdorP0BQX-5QUvERZ7CgntLysKxPYR85LNkkQ-ODVQlzCBgHDwYGwBEtb1wyzIiqYOAGOFOhRLG73H-MUdJY1ZFjTgiSsk2gQgTHDHU_Mnn5ewYy4nGfZAENFgsXyYdMtYQ&sa=X&ved=2ahUKEwi57se2n5-HAxV0TGwGHXezCCsQtKgLegQIDRAB&biw=1536&bih=703&dpr=1.25")

#tell to selenium that you have to go to certain height
height = driver.execute_script("return document.body.scrollHeight")
print(height)

#selenium to scroll up to that height
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")