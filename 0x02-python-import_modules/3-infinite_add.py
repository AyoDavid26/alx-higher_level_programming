#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total_sum = 0
    for i in range(1, len(argv)):
        total_sum += int(argv[i])
    print("{}".format(total_sum))
