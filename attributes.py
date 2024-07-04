import requests
from bs4 import BeautifulSoup

url ="https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
print(soup.div.ul)
print(soup.div.a)
print(soup.div.p)

tags = soup.div
print(tags.attrs)

tags = soup.header
atb = (tags.attrs)
print(atb["class"])

print(atb["role"])




