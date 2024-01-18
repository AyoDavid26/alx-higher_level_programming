#!/usr/bin/python3
if __name__ =="__main__":
    from hidden_4 import *
    my_func = dir()
    for i in range (0, len(my_func)):
        if my_func[i][:2] != "__":
            print("{:s}".format(my_func[i]))
