# FIle -> Settings -> Project Interpreter -> Click on a package
# get packages requests, and bs4
# typing this into console works
# ALT + SHIFT + E executes the selcted line in Python Console


import requests
import urllib
from bs4 import BeautifulSoup

# requests the web page download
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page
page.status_code

# 200 is right code response and means you downloaded the page

page.content

# create a soup class
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

list(soup.children)
[type(item) for item in list(soup.children)]
html = list(soup.children)[2]
list(html.children)
print(html)

# extract text from inside <p> tag by first isolating the body
body = list(html.children)[3]
list(body.children)
print(body)
# isolate <p>
p = list(body.children)[1]
# extract text in p
p.get_text()
print(p.prettify())

# finding all instances of a tag at once
soup.find_all('p')
# extract text from the list
soup.find_all('p')[0].get_text()
# find only the first <p> on the page list
soup.find('p')