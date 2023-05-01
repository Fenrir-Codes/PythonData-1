#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    l = []
    for row in a:
        l.append(row)
    return l

def get_columns(a):
    l = []
    for col in a.transpose():
        l.append(col) 
    return l

# def get_columns(a):
#     return get_rows(a.T))

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
