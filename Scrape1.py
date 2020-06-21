
import requests
from bs4 import BeautifulSoup
# import pandas as pd

page = requests.get('https://www.newegg.com/DailyDeal.aspx?name=DailyDeal')

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

deals = soup.find(id='bodyArea')

# print(deals)

items = deals.find_all(class_='item-title')

print(items)

names = items[0]

# names = items.find_all(title='View Details')

# print(names)

# livar = soup.find_all('li')

# print(livar)

# for li in soup.find_all('li'):
#     for div in li.find_all('li'):
#         print(li)
