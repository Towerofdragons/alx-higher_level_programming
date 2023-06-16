#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    largest = 0
    for i in a_dictionary:
        if a_dictionary[i] > largest:
            largest = a_dictionary[i]
    return largest
