# Current day weather data

import datetime
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?CityName=Pinconning&state=MI&site=DTX&textField1=43.8579&textField2=-83.9646&e=0")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())
print("")

# print todays date and time
time1 = datetime.datetime.now()
print(time1)

# extracts the classes and prints
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)

# extracts the img text and prints
img = tonight.find("img")
desc = img['title']

print(desc)