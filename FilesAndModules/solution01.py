#!/usr/bin/env python3

line_number = 0

with open("./dummy.txt") as file_ref:
    for line in file_ref:
        line_number = line_number + 1
        # Without line.rstrip() you get an additional blank line.
        print("{}. {}".format(str(line_number), line.rstrip()))