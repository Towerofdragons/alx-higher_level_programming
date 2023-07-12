#!/usr/bin/python3
"""
Module defines 'write_file'.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written.
    """

    written = 0
    with open(filename, 'w', encoding="utf-8") as f:
        written = f.write(text)

    return written
