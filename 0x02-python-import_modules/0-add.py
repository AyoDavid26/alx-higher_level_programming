#!/usr/bin/python3
if __name__ == "__main__":
    """ a  program to import a simple function from a simple file"""
    from add_0 import add
    a = 1
    b = 2
    print ("{} + {} = {}".format(a,b, add(a,b)))
