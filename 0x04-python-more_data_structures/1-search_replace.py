#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp = my_list.copy()
    cp = [x if x != search else replace for x in my_list]
    return cp
