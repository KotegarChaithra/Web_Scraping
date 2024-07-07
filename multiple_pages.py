import requests
from bs4 import BeautifulSoup

for i in range(2,11):
    url ="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text,"lxml")
    # print(soup)

    next_page = soup.find("a",class_="_9QVEpD").get("href")
    # print(next_page)
    complete_next_page = "https://www.flipkart.com/"+next_page
    print(complete_next_page)

    url = complete_next_page
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")