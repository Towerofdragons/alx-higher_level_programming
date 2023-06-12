#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new_string = ""
    for char in range(length):
        if my_string[char] != "c" and my_string[char] != "C":
            new_string = new_string +  my_string[char]
    return new_string
