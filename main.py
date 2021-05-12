import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '!@#$%^&*(){}[];,./+-*=_\\'

upper, lower, nums, sym = True, True, True, True

password = ''
all = ''

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if sym:
    all += symbols

amount = int(input('Enter Number of Passwords to be Generated: '))
length = int(input('Enter the Length of Your Password: '))

for x in range(amount):
    password = ''.join(random.sample(all, length))

    print(f'Password {x + 1} : {password}')
