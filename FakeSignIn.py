# source https://www.youtube.com/watch?v=UtNYzv8gLbs

import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://example.fakewebsite.target.com/indexblahblahblah'

names = json.loads(open(r'C:\gnamesjs').read())
print(names)
for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(8))
    print(username, password)
    #requests.post(url, allow_redirects=False, data={
     #   'field where the username is getting sent': username,
     #   'field where the password is being sent': password
    #})
print(username,password)
