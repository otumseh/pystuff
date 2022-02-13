# file downloader using curl or wget
# test line

# stuff needed and panda lists formatting
# import csv
import os
# import time
# import requests
from selenium import webdriver
# from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('max_colwidth', 140)
pd.set_option('expand_frame_repr', False)


#
class Primewirebin:
    def __init__(self):
        space = " "
        # forslashspace = "\ "
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        site = (input("Input url: "))
        pathconst = "/home/nosmo/D_2tb/temp/"
        # pathINP = (input("Input destination path: "))
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
        # askcsv = (input("Do you want a csv? 'y' or 'n': "))
        self.driver = webdriver.Chrome("./chromedriver", options=options)
        # self.driver.get("https://www.ebay.com/")
        # time.sleep(4)
        # self.driver.find_element_by_xpath("//*[@id='gh-ac-box2']").click()
        # searchbox = self.driver.find_element_by_css_selector("#gh-ac")
        # time.sleep(3)
        # searchbox.send_keys(search1)
        # startsearch = self.driver.find_element_by_css_selector("#gh-btn")
        # time.sleep(1)
        # startsearch.click()
        # time.sleep(4)
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
#             listend = pd.concat([list1, list2], ignore_index=True)
#             listend.to_csv("/home/nosmo/Documents/" + search1 + ".csv")
# close selenium browser head
        self.driver.close()
