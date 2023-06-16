#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    largest = 0
    largest_key = ""
    for i in a_dictionary:
        if a_dictionary[i] > largest:
            largest = a_dictionary[i]
            largest_key = i
    return largest_key
