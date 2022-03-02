# file downloader using curl or wget
# test line

# stuff needed and panda lists formatting
# import csv
# import numpy as np
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('max_colwidth', 140)
pd.set_option('expand_frame_repr', False)


# bot to dl movies
class Primewirebin:
    def __init__(self):

    # get user's search
        selectmedia = (input("Type 'M' for a Movie search and 'T' for TV."))

        if selectmedia == "M" or "m":
            search0 = (input("Input Movie title: "))
        else:
            search1 = (input("Input TV series: "))
    # selenium
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome("./chromedriver", options=options)
        self.driver.get("https://www.primewire.vc/")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='search_term']").click()
        searchbox = self.driver.find_element_by_css_selector("#search_term")
        time.sleep(3)
        searchbox.send_keys(search0)
        searchbox.send_keys(Keys.ENTER)

        searchres = self.driver.current_url
        res = requests.get(searchres)
        primewiresoup = BeautifulSoup(res.text, "lxml")
        elements = primewiresoup.select("div.index_item.index_item_ie a")
        print(elements[0]["href"])
        firstpos = (elements[0]["href"])
        print(firstpos)
        movpage = "https://www.primewire.vc" + firstpos
        self.driver.get(movpage)
        time.sleep(1)
        # startsearch = self.driver.find_element_by_css_selector("#button.btn")
        # time.sleep(1)
        # startsearch.click()
        # time.sleep(3)
# get current url
        url = self.driver.current_url
        print(url)
        page = requests.get(url)
# scrape host options
# create dbs to take data from scrape targets
        item_qs = []
        sizes = []
        hostsites = []
        gotos = []

        data = page.text
        soup = BeautifulSoup(data)

        listings = soup.find_all('table', attrs={'class': 'movie_version'})
        # print(listings)
        for listing in listings:
            prod_name = " "
            # prod_price = " "
            # prod_shipping = " "
            for name in listing.find_all('td', attrs={'class': "link_version_quality"}):
                if str(name.find(text=True, recursive=False)) != "None":
                    prod_name = str(name.find(text=True, recursive=False))
                    item_qs.append(prod_name)
                    print(prod_name)
            # prices
            if prod_name != " ":
                size = listing.find('span', attrs={'class': "quality_tag"})
                # pricestr = str(price.find(text=True, recursive=False))
                sizes.append(size)
                print(size)
                # shippings
                # shipping = [sc.get_text() for sc in listing.select(".s-item .s-item__shipping.s-item__logisticsCost")]
                hostsite = listing.find('span', attrs={'class': "version-host"})
                # prod_shipping = str(shipping.find(text=True, recursive=False))
                hostsites.append(hostsite)
                print(hostsite)

                starturl = self.driver.current_url
                res = requests.get(starturl)
                newsoup = BeautifulSoup(res.text, "lxml")
                elements = newsoup.select("propper-link.popper.ico-btn a")
                goto = elements[0]["href"]
                gotos.append(goto)
                # print(elements[-1]["href"])
                # buyitnow = (elements[-1]["href"])
                # print(buyitnow)
                # self.driver.get(buyitnow)
        # print checks
        print(len(item_qs))
        print(len(sizes))
        print(len(hostsites))
        # print(hostsites)
        #
        # list0len = (len(item_qs))
        # list1len = (len(sizes))
        # list2len = (len(hostsites))
        # list3len = (len(item_names))
        # list4len = (len(prices))
        # list5len = (len(shippings))
# put into pandas df
        output = pd.DataFrame({"Name": item_qs, "Price": sizes, "Shipping": hostsites})
        print(output)
# get option from user an option and go to it
        selecthost = input("Select the index of the host you wish to use: ")

# download
        space = " "
        # forslashspace = "\ "
        site = (input("Input url: "))
        pathconst = "/home/nosmo/D_2tb/temp/"
        # pathINP = (input("Input destination path: "))
        # askcsv = (input("Do you want a csv? 'y' or 'n': "))
        name1 = (input("Input file name: "))
        # name1.replace(' ', ' ')
        namespace = name1 + space
        pathconst1 = pathconst + namespace
        print(pathconst1)
        combo1 = pathconst1 + site
        print(combo1)
        os.system(f'curl --output {combo1}')



        # os.system(f'wget -O {combo1}')
        # os.system(f'for file in {pathconst}; do mv "$file" `echo $file | tr '_' ' ' ; done')
        # self.driver.find_element_by_css_selector("li.fake-tabs__item:nth-child(4)").click()

# current location and print check page 1 and 2
#         url = self.driver.current_url
#         print(url)
#         page = requests.get(url)
#         url2 = url + "&_pgn=2"
#         print(url2)
#         page2 = requests.get(url2)
# # scrape date
#         soup = BeautifulSoup(page.content, 'html.parser')
#         soup2 = BeautifulSoup(page2.content, 'html.parser')
#
#         fullpage = soup.find(id="mainContent")
#         fullpage2 = soup2.find(id="mainContent")
#
#         short_descs = [sd.get_text() for sd in fullpage.select(".s-item .s-item__title")]
#         prices1 = [p.get_text() for p in fullpage.select(".s-item .s-item__price")]
#         shippingcost = [sc.get_text() for sc in fullpage.select(".s-item .s-item__logisticsCost")]
#         short_descs2 = [sd.get_text() for sd in fullpage2.select(".s-item .s-item__title")]
#         prices2 = [p.get_text() for p in fullpage2.select(".s-item .s-item__price")]
#         shippingcost2 = [sc.get_text() for sc in fullpage2.select(".s-item .s-item__logisticsCost")]
# # make panda list(s)
#         list1 = pd.DataFrame({
#             "Description": short_descs,
#             "Price": prices1,
#             "Shipping": shippingcost
#         })
#         list2 = pd.DataFrame({
#             "Description": short_descs2,
#             "Price": prices2,
#             "Shipping": shippingcost2
#         })
# # print check lists
#         print("")
#         print(list1)
#         time.sleep(3)
#         print(list2)
#         time.sleep(10)
# # if csv ? answer is y create csv
#         if askcsv == "y":
#             csvpath = (input("Where do you want the csv?: "))
#             search2 = csvpath + search1
#             listend = pd.concat([list1, list2], ignore_index=True)
#             listend.to_csv(search2 + ".csv")
# close selenium browser head
        self.driver.close()
