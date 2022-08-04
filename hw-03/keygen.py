#!/usr/bin/env python3
import os

if __name__ == '__main__':
    username = input('Username: ')

    if (len(username) > 30):
        print('Invalid username!')
        os.exit(1)

    passwd = 0
    for i in username.upper():
        if (i >= 'Z'):
            i = chr(ord(i) - 0x20)
        passwd = passwd + ord(i)

    passwd ^= 0x5678 ^ 0x1234
    print('Password: {}'.format(passwd))
