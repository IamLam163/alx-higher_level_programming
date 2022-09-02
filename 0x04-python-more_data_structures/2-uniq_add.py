#!/usr/bin/python
def uniq_add(my_list=[]):
    new_list = set(my_list)
    result = 0
    for i in new_list:
        result += i
    return new_list
        
