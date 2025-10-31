import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digit = "0123456789"
symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
        all += uppercase_letters

if lower:
        all += lowercase_letters

if nums:
        all += digit

if symbols:
        all += symbols

length = 20
amount = 10

for x in range (amount):
        password = "".join(random.sample(all, length ))
        print(password)