# Bot for entering place and extracting Current day weather data

import datetime
import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup


class WeaTher:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        #
        search1 = (input("Enter City, St or zip code : "))
        #
        self.driver = webdriver.Chrome("./chromedriver", options=options)
        self.driver.get("https://www.weather.gov/")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='inputstring']").click()
        searchbox = self.driver.find_element_by_css_selector("#inputstring")
        time.sleep(2)
        searchbox.send_keys(search1)
        time.sleep(2)
        startsearch = self.driver.find_element_by_css_selector("#btnSearch")
        time.sleep(1)
        startsearch.click()
        time.sleep(1)
# scrape
        url = self.driver.current_url
        # print(url)
        page = requests.get(url)
# soups
        soup = BeautifulSoup(page.content, 'html.parser')
        now = soup.find(id="current_conditions-summary")
        seven_day = soup.find(id="seven-day-forecast")
        forecast_items = seven_day.find_all(class_="tombstone-container")
        tonight = forecast_items[0]
        print("")
# print todays date and time
        time1 = datetime.datetime.now()
        print(time1)
# extracts the classes and prints
        period = tonight.find(class_="period-name").get_text()
        short_desc = tonight.find(class_="short-desc").get_text()
        currenttemp = now.find(class_="myforecast-current-lrg").get_text()
        temp = tonight.find(class_="temp").get_text()
# main print
        print(period)
        print(short_desc)
        print("Current: ", currenttemp)
        print(temp)
# extracts the img text and prints
        img = tonight.find("img")
        desc = img['title']
        print(desc)
# close driver
        self.driver.close()
