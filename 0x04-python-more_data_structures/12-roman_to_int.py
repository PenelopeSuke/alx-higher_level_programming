#!/usr/bin/python3

def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    s = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[c]] >= s:
                r += val[roman_string[c]]
            else:
                r -= val[roman_string[c]]
                s = val[roman_string[c]]
                return r
