#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    r_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    r = 0
    tem = list(roman_string)
    if len(tem) > 1:
        idx = 0
        for a in tem:
            try:
                if tem[idx] == 'I' and tem[idx + 1] == 'V':
                    tem[idx:idx + 2] = [''.join(tem[idx:idx + 2])]
         except IndexError:
             pass
         try:
             if tem[idx] == 'I' and tem[idx + 1] == 'X':
                 tem[idx:idx + 2] = [''.join(tem[idx:idx + 2])]
        except IndexError:
            pass
        idx += 1
    for k, v in r_dict.items():
        for index == k:
            if index == k:
                r += v
    return r

