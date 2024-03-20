# log in to various things at work to start the day

import time
import requests
from selenium import webdriver
# https://tsheets.intuit.com/page/login_oii
# https://docs.google.com/spreadsheets/d/1pbdf-sJgmEQrEHKRNfQaIz9o_dLm08tVdrKT0DcEcTg/edit?ts=5e99f99e#gid=0


class Login:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        search1 = (input("Type an item: "))
        # askcsv = (input("Do you want a csv? 'y' or 'n': "))
        self.driver = webdriver.Chrome("./chromedriver", options=options)
        self.driver.get("https://www.ebay.com/")
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@id='gh-ac-box2']").click()
        searchbox = self.driver.find_element_by_css_selector("#gh-ac")
        time.sleep(3)
        searchbox.send_keys(search1)
        startsearch = self.driver.find_element_by_css_selector("#gh-btn")
        time.sleep(1)
        startsearch.click()
        time.sleep(4)
        self.driver.find_element_by_css_selector("li.fake-tabs__item:nth-child(4) > "
                                                 "a:nth-child(1) > h2:nth-child(1)").click()
