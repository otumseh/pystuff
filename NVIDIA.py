# lets scrape NVIDIA shop

import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.nvidia.com/en-us/geforce/products/10series/geforce-store/")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#test1 = soup.select("div p")
#test2 = soup.select("div a")
#print(test1)
#print(test2)
nvidiasite = soup.find(id="page-content")
graphicscards = nvidiasite.find_all(class_="sectionWrapper parbase section")
tonight = graphicscards[0]

# print(tonight.prettify())

cardname = tonight.find(class_="title color-body-copy ").get_text()
# price1 = tonight.find(class_="product-row__item js-product-item").get_text()
# price2 = tonight.find

print("")
print(cardname)
# print(price1)

cardname_tags = nvidiasite.select(".sectionWrapper parbase section .title color-body-copy ")
cardnames = [pt.get_text() for pt in cardname_tags]

print(cardnames)

