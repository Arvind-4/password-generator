import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

upper, lower, nums, sym = True, True, True, True

password = ""
_all = ""

if upper:
    _all += uppercase_letters

if lower:
    _all += lowercase_letters

if nums:
    _all += digits

if sym:
    _all += symbols

amount = int(input("Enter number of passwords to be generated: "))
length = int(input("Enter the length of your password: "))

for x in range(amount):
    password = "".join(random.sample(_all, length))
    print(f"Password {x + 1} : {password}")
