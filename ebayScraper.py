# scrape ebay for specific stuff
# looking for an i7 3770

import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('max_colwidth',140)
pd.set_option('expand_frame_repr', False)

page = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=i7+3770+&_sacat=0&LH_BIN=1&Processor%2520Model=Intel%2520Core%2520i7%252D3770")
soup = BeautifulSoup(page.content, 'html.parser')
fullpage = soup.find(id="mainContent")
entry1 = fullpage.find_all(class_="s-item")
i73770 = entry1[0]

# print(i73770.prettify())

desc = i73770.find(class_="s-item__title").get_text()
price = i73770.find(class_="s-item__detail s-item__detail--primary").get_text()
# shipping = i73770.find(class_="s-item__detail s-item__detail--primary").get_text()

# print("")
# print(desc)
# print(price)
# print(shipping)

desc_tags = fullpage.select(".s-item .s-item__title")
descs = [pt.get_text() for pt in desc_tags]
price_tags = fullpage.select(".s-item .s-item__price")
prices = [pt1.get_text() for pt1 in price_tags]
# shipping_tags = fullpage.select(".s-item .s-item__shipping s-item__logisticsCost")
# shippings = [pt2.get_text() for pt2 in shipping_tags]

# print("")
# print(descs)
# print(prices)
# print(shippings)

short_descs = [sd.get_text() for sd in fullpage.select(".s-item .s-item__title")]
prices1 = [p.get_text() for p in fullpage.select(".s-item .s-item__price")]
shippingcost = [sc.get_text() for sc in fullpage.select(".s-item .s-item__logisticsCost")]

# print("")
# print(short_descs)
# print(prices1)
# print(shippingcost)

list1 = pd.DataFrame({
         "desc": short_descs,
         "price": prices1,
         "shipping": shippingcost
     })

print("")
print(list1)