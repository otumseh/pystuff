# ebay scraper using selenium
# test line

# grab stuff needed and panda lists formatting
# import csv
# import numpy as np
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
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
        print(elements[2]["href"])
        buyitnow = (elements[2]["href"])
        print(buyitnow)
        self.driver.get(buyitnow)
        time.sleep(1)
        # buyitnow = self.driver.find_element_by_css_selector("li.fake-tabs__item.btn")
        # buyitnow.click()
# current location check and print page 1 and 2
        url = self.driver.current_url
        print(url)
        page = requests.get(url)
        url2 = url + "&_pgn=2"
        print(url2)
        page2 = requests.get(url2)
# scrape descriptions, prices, shipping data for 2 pages of results
        soup = BeautifulSoup(page.content, 'html.parser')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        fullpage = soup.find(id="mainContent")
        fullpage2 = soup2.find(id="mainContent")

        # itembins = [ib.get_text() for ib in fullpage.select(".s-item")]
        # print(itembins)

        short_descs1 = [sd.get_text() for sd in fullpage.select(".s-item .s-item__title")]
        prices1 = [p.get_text() for p in fullpage.select(".s-item .s-item__price")]
        shippingcost1 = [sc.get_text() for sc in fullpage.select(".s-item .s-item__shipping.s-item__logisticsCost")]

        short_descs2 = [sd.get_text() for sd in fullpage2.select(".s-item .s-item__title")]
        prices2 = [p.get_text() for p in fullpage2.select(".s-item .s-item__price")]
        shippingcost2 = [sc.get_text() for sc in fullpage2.select(".s-item .s-item__shipping.s-item__logisticsCost")]
# make pandas data frames
    # Page 1 lists
        # Descriptions for page 1
        list0 = pd.DataFrame({"Description": short_descs1})
        list0["Description"] = list0["Description"].fillna(0)
        list0 = list0.to_numpy()
        entry1 = (list0[0])
        print(entry1)
        if entry1 == "Shop on eBay":
            check1 = True
            list0 = pd.DataFrame({"Description": short_descs1})
            list0 = list0.drop(labels=0, axis=0)
        else:
            list0 = pd.DataFrame({"Description": short_descs1})
            check1 = False
        # Prices for page 1
        list1 = pd.DataFrame({"Price": prices1})
        list1["Price"] = list1["Price"].fillna(0)
        list1 = list1.to_numpy()
        entry2 = (list1[0])
        print(entry2)
        if entry2 == "$20.00" and check1 is True:
            list1 = pd.DataFrame({"Price": prices1})
            list1 = list1.drop(labels=0, axis=0)
        else:
            list1 = pd.DataFrame({"Price": prices1})

        # Shipping costs for page 1
        list2 = pd.DataFrame({"Shipping": shippingcost1})
        list2["Shipping"] = list2["Shipping"].fillna(0)
        # grab data frame lengths page 1
        list0len = (len(short_descs1))
        list1len = (len(prices1))
        list2len = (len(shippingcost1))
    # Page 2 lists
        # Descriptions for page 2
        list3 = pd.DataFrame({"Description": short_descs2})
        list3["Description"] = list3["Description"].fillna(0)
        list3 = list3.to_numpy()
        entry3 = (list3[0])
        print(entry3)
        if entry3 == "Shop on eBay":
            check2 = True
            list3 = pd.DataFrame({"Description": short_descs2})
            list3 = list3.drop(labels=0, axis=0)
        else:
            list3 = pd.DataFrame({"Description": short_descs2})
            check2 = False
        # Prices for page 2
        list4 = pd.DataFrame({"Price": prices2})
        list4["Price"] = list4["Price"].fillna(0)
        list4 = list4.to_numpy()
        entry4 = (list4[0])
        print(entry4)
        if entry4 == "$20.00" and check2 is True:
            list4 = pd.DataFrame({"Price": prices2})
            list4 = list4.drop(labels=0, axis=0)
        else:
            list4 = pd.DataFrame({"Price": prices2})
        # Shipping costs for page 2
        list5 = pd.DataFrame({"Shipping": shippingcost2})
        list5["Shipping"] = list5["Shipping"].fillna(0)
        # grab data frame lengths page 2
        list3len = (len(short_descs2))
        list4len = (len(prices2))
        list5len = (len(shippingcost2))
# check for page duplicates/single page listing check and print check lists
        if list0len == list3len and list1len == list4len and list2len == list5len:
            print(list0len, list1len, list2len)
            print("There is only one page worth of entries.")
            print("")
            print(list0, " ", list1, " ", list2)
            time.sleep(2)
        # if csv ? answer is y create csv for 1 page
            if askcsv == "y":
                csvpath = (input("Where do you want the csv?: "))
                search2 = csvpath + search1
                listend = pd.concat([list0, list1, list2], ignore_index=True)
                listend.to_csv(search2 + ".csv")
        else:
            print(list0len, list1len, list2len)
            print(list3len, list4len, list5len)
            print("There are more than one page worth on entries.")
            print("")
            print(list0, list1, list2)
            time.sleep(2)
            print(list3, list4, list5)
            time.sleep(4)
        # if csv ? answer is y create csv for 2 pages
            if askcsv == "y":
                csvpath = (input("Where do you want the csv?: "))
                search2 = csvpath + search1
                listend = pd.concat([list0, list1, list2, list3, list4, list5], ignore_index=True)
                listend.to_csv(search2 + ".csv")
# close selenium browser head
        self.driver.close()
