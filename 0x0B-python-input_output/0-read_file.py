#!/usr/bin/python3
"""
Module defines the read_file function.
"""


def read_file(filename=""):
    """
    Reads a text file of UTF-8 format.
    """

    with open("my_file_0.txt", 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
