# Extended Weather data for current and next 4 days

import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('max_colwidth',164)
pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

page = requests.get("https://forecast.weather.gov/MapClick.php?CityName=Pinconning"
                    "&state=MI&site=DTX&textField1=43.8579&textField2=-83.9646&e=0")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

# extract everything at once
# need Pandas

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# print(short_descs)
# print(temps)
# print(descs)

# pandas data frame
weather = pd.DataFrame({
        "Basic Description": short_descs,
        "Period": periods,
        "Temperature": temps,
        "Full Description": descs
    })

print(weather)

# pull out number (temperatures)
# temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
# weather["temp_num"] = temp_nums.astype('int')
# print(temp_nums)

# find the mean of the temps
# weather["temp_num"].mean()

# select rows for night only
# is_night = weather["temp"].str.contains("Low")
# weather["is_night"] = is_night
# print(is_night)
