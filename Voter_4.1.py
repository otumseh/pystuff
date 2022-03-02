# ebay scraper using selenium
# test line

# grab stuff needed and panda lists formatting
# import csv
# import numpy as np
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
# from functools import reduce
import pandas as pd
# from scipy import stats
pd.set_option('max_colwidth', 140)
pd.set_option('expand_frame_repr', False)


# bot setup and user input, open buy it now page 1
class EbayBIN:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
# Collect input and execute search
        search1 = (input("Type an item: "))
        askcsv = (input("Do you want a csv? 'y' or 'n': "))
        self.driver = webdriver.Chrome("./chromedriver", options=options)
        self.driver.get("https://www.ebay.com/")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='gh-ac-box2']").click()
        searchbox = self.driver.find_element_by_css_selector("#gh-ac")
        time.sleep(2)
        searchbox.send_keys(search1)
        startsearch = self.driver.find_element_by_css_selector("#gh-btn")
        time.sleep(1)
        startsearch.click()
        time.sleep(2)
# gets buy it now tab for chosen item
        starturl = self.driver.current_url
        res = requests.get(starturl)
        ebaysoup = BeautifulSoup(res.text, "lxml")
        elements = ebaysoup.select("li.fake-tabs__item.btn a")
        print(elements[-1]["href"])
        buyitnow = (elements[-1]["href"])
        print(buyitnow)
        self.driver.get(buyitnow)
        time.sleep(1)
        # buyitnow = self.driver.find_element_by_css_selector("li.fake-tabs__item.btn")
        # buyitnow.click()
    # current location check and print check page 1 and 2
        url = self.driver.current_url
        print(url)
        page = requests.get(url)
        url2 = url + "&_pgn=2"
        print(url2)
        page2 = requests.get(url2)

    # create dbs to take data from scrape targets
        item_names = []
        prices = []
        shippings = []

        data = page.text
        soup = BeautifulSoup(data)

        listings = soup.find_all('li', attrs={'class': 's-item'})

        for listing in listings:
            prod_name = " "
            # prod_price = " "
            # prod_shipping = " "
            for name in listing.find_all('h3', attrs={'class': "s-item__title"}):
                if str(name.find(text=True, recursive=False)) != "None":
                    prod_name = str(name.find(text=True, recursive=False))
                    item_names.append(prod_name)
            # prices
            if prod_name != " ":
                price = listing.find('span', attrs={'class': "s-item__price"})
                pricestr = str(price.find(text=True, recursive=False))
                prices.append(pricestr)
                # print(price)
            # shippings
                shipping = [sc.get_text() for sc in listing.select(".s-item .s-item__shipping.s-item__logisticsCost")]
                # prod_shipping = str(shipping.find(text=True, recursive=False))
                shippings.append(shipping)
                # print(shipping)
        # print checks
        print(len(item_names))
        print(len(prices))
        print(len(shippings))
        # print(shippings)
#
        list0len = (len(item_names))
        list1len = (len(prices))
        list2len = (len(shippings))
        list3len = (len(item_names))
        list4len = (len(prices))
        list5len = (len(shippings))
        # output = pd.DataFrame({"Name": item_names, "Price": prices})
        output = pd.DataFrame({"Name": item_names, "Price": prices, "Shipping": shippings})
        # shipout = pd.DataFrame({"Shipping": shippings})
        print(output)
        # print(shipout)
        # check for page duplicates/single page listing check and print check lists
        if list0len == list3len and list1len == list4len and list2len == list5len:
            print(list0len, list1len, list2len)
            print("There is only one page worth of entries.")
            # print("")
            # print(list0, " ", list1, " ", list2)
            time.sleep(2)
            # if csv ? answer is y create csv for 1 page
            if askcsv == "y":
                csvpath = (input("Where do you want the csv?: "))
                search2 = csvpath + search1
                # listend = pd.concat([list0, list1, list2], ignore_index=True)
                output.to_csv(search2 + ".csv")
        else:
            print(list0len, list1len, list2len)
            print(list3len, list4len, list5len)
            print("There are more than one page worth on entries.")
            print("")
            print(item_names, prices, shippings)
            time.sleep(2)
            print(item_names, prices, shippings)
            time.sleep(4)
            # if csv ? answer is y create csv for 2 pages
            if askcsv == "y":
                csvpath = (input("Where do you want the csv?: "))
                search2 = csvpath + search1
                listend = pd.concat([item_names, prices, shippings, item_names, prices, shippings], ignore_index=True)
                listend.to_csv(search2 + ".csv")
        self.driver.close()
