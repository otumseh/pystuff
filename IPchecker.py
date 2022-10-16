"""
This program checks external and internal IPs and other info
"""

# import requests
# import sys
# import dfwinreg
import socket
import platform
import psutil
from requests import get

print("")

# info using psutil
cpucount = psutil.cpu_count()
cpucountphys = cpucount/2
cpu2 = psutil.cpu_freq()
cpu3 = psutil.cpu_stats()
boot1 = psutil.boot_time()
user = psutil.users()
# net1 = psutil.net_if_addrs()

print("Logical cores =", cpucount)
print("Physical cores =", cpucountphys)
print(cpu2)
print(cpu3)
print(boot1)
print(user)
# print(net1)

print("")
# info using platform and sys
name = platform.uname()
cpu = platform.processor()
# winver = sys.getwindowsversion()

print(name)
print("CPU architecture =", cpu)
# print(winver)

print("")
# Gets external IP through scraping
ip = get('https://api.ipify.org', timeout=5).text
print("Your external IP is ", ip)

# Gets internal IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Your internal IP is ", s.getsockname()[0])
s.close()

# trying to scape from google answer list to what is my ip
# from bs4 import BeautifulSoup

# page = requests.get("https://www.google.com/search?q=What+is+my+ip&oq=
#                    "What+is+my+ip&aqs=chrome..69i57.3309j0j8&sourceid=chrome&ie=UTF-8")
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# list(soup.children)
# ipadd = soup.find(class_="pIpgAc.xyYs1c.XO51F.xsLG9d")
# print(ipadd)

# ipadd = soup.find(id="search")
# ipitem = ipadd.find_all(class_="")
# ipnow = ipitem[0]
# print(ipnow.prettify())
