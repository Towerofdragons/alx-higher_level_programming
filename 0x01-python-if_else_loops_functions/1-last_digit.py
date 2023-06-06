#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number *= -1
    last_digit = (number % 10) * -1
    number *= -1
else:
    last_digit = number % 10

res = f"Last digit of {number} is {last_digit} "
if last_digit > 5:
    res += "and is greater than 5"
elif last_digit == 0:
    res += "and is 0"
elif last_digit < 6:
    res += "and is less than 6 and not 0"

print(res)
