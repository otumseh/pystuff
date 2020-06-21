# Scraper for a i7 3770k

import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('max_colwidth', 140)
pd.set_option('expand_frame_repr', False)

page = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=i7+3770k&_sacat=0&LH_BIN=1&rt=nc&Processor%2520Model=Intel%2520Core%2520i7%252D3770K&_dcat=164")
# page2 = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=i7+3770+&_sacat=0&LH_BIN=1&Processor%2520Model=Intel%2520Core%2520i7%252D3770&_pgn=2")
soup = BeautifulSoup(page.content, 'html.parser')
# soup2 = BeautifulSoup(page2.content, 'html.parser')
fullpage = soup.find(id="mainContent")
# fullpage2 = soup2.find(id="mainContent")
entry1 = fullpage.find_all(class_="s-item")
# entry2 = fullpage2.find_all(class_="s-item")
# i73770 = entry1[0]

short_descs = [sd.get_text() for sd in fullpage.select(".s-item .s-item__title")]
prices1 = [p.get_text() for p in fullpage.select(".s-item .s-item__price")]
shippingcost = [sc.get_text() for sc in fullpage.select(".s-item .s-item__logisticsCost")]
# print(shippingcost)

# short_descs2 = [sd.get_text() for sd in fullpage2.select(".s-item .s-item__title")]
# prices2 = [p.get_text() for p in fullpage2.select(".s-item .s-item__price")]
# shippingcost2 = [sc.get_text() for sc in fullpage2.select(".s-item .s-item__logisticsCost")]

a = {"desc": short_descs,
    "price": prices1}
    # "shipping": shippingcost}

df = pd.DataFrame.from_dict(a, orient='columns')

# df.transpose()
# df1 = df.isnull()
print("")
print(df)

# list1 = pd.DataFrame({
#     "desc": short_descs,
#     "price": prices1,
#     "shipping": shippingcost
#      })
# list1.fillna(0)

# list2 = pd.DataFrame({
#     "desc": short_descs2,
#     "price": prices2,
#     "shipping": shippingcost2
#      })

# print("")
# print(list1)
# print(list2)
