#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
        oper = argv[2]
        a, b = int(argv[1]), int(argv[3])
        if oper == "+":
            print('{} + {} = {}'.format(a, b, add(a, b)))
        elif oper == "-":
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif oper == "*":
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        elif oper == "/":
            print('{} / {} = {}'.format(a, b, div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
