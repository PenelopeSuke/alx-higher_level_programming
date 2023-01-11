#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    tem = dict(a_dictionary)
    for k, v in tem.items():
        tem[k] = v * 2
    return tem
