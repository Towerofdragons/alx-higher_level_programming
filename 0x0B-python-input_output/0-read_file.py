#!/usr/bin/python3
"""
Module defines the read_file function.
"""


def read_file(filename=""):
    """
    Reads a text file of UTF-8 format.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        #for line in f:
        print(f.read(), end="")
