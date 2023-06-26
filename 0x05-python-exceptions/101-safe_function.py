#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as Err:
        print("Exception: {}".format(Err), file=sys.stderr)
        return None
