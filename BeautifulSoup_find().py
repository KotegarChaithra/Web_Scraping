import requests
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")
#we are searching for <h4> tag
# print(soup.find('div'))

price = soup.find("h4",{"class":"price float-end card-title pull-right"})
# print(price.string)

desc = soup.find("p",class_= "description card-text")
print(desc.string)

