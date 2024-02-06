#!/usr/bin/python3

def raise_exception():
    try:
        result = 10 + 'x'
    except TypeError as te:
        raise te
