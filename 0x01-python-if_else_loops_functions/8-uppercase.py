#!/usr/bin/python3

def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) >= 97:
            print("{:c}".format(ord(str[char]) - 32), end="" if char != (len(str) - 1) else "\n")
        else:
            print(str[char], end="" if char != (len(str) - 1) else "\n")
uppercase("Best")
