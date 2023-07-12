#!/usr/bin/python3
"""
Module defines the 'append_write' function.
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.
    """

    written = 0
    with open("filename", 'a') as f:
        written = f.write(text)
    return written
