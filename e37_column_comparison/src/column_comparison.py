#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    # print(np.sum((0 < a) & (a < 10)))
    # a = np.array([1,3,4])
    # b = np.array([2,2,7])
    # c = a > 0
    # print(a[:,1])
    # print(a[:,-2])
    mask = a[:,1] > a[:,-2]
    # print(mask)
    # print(a[mask])
    return a[mask]
    
def main():
    arr = np.array([[8, 9, 3, 8, 8], 
                   [0, 5, 3, 9, 9],
                   [5, 7, 6, 0, 4],
                   [7, 8, 1, 6, 2],
                   [2, 1, 3, 5, 8]])
    print(column_comparison(arr))

if __name__ == "__main__":
    main()
