import requests
from bs4 import BeautifulSoup

# Searching for tags by class and id

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup
print(soup)

# search for any p tag that has the class outer-text
soup.find_all('p', class_='outer-text')

# look for any tag that has the class outer-text
soup.find_all(class_="outer-text")

# search for elements by id
soup.find_all(id="first")

# CSS selectors
# p a — finds all a tags inside of a p tag.
# body p a — finds all a tags inside of a p tag inside of a body tag.
# html body — finds all body tags inside of an html tag.
# p.outer-text — finds all p tags with a class of outer-text.
# p#first — finds all p tags with an id of first.
# body p.outer-text — finds any p tags with a class of outer-text inside of a body tag.

# find all the p tags in our page that are inside of a div
soup.select("div p")