#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    index_count = 0

    for index in new_string:
        if index == 'c' or index == 'C':
            new_string[index_count] = ""
            index_count += 1
        return "".join(new_string)
