#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    r = 0.0
    s_list = list(t[0] * t[1] for t in my_list)
    w_list = list(t[1] for t in my_list)
    r = sum(s_list) / sum(w_list)
    return r
