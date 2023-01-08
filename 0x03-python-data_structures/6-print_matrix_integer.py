#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for k in range(len(matrix)):
        for l in range(len(matrix[k])):
                print("{:d}".format(matrix[k][l]), end="")
                if l != (len(matrix[k]) - 1):
                    print(" ", end="")
      print("")
