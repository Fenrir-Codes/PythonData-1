#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a = np.arange(n) # row
    b = np.arange(n).reshape(n,1) # column
    c = a*b # broadcasting, column og row udfylder sig selv, 
    # så den passer med den modsatte. Altså a forekommer b gange og samme for b.
    # 
    #* broadcast a bliver til: 
    # [[0,1,2,3]
    # [0,1,2,3]
    # [0,1,2,3]
    # [0,1,2,3]] 
    # 
    # og broadcast b bliver til: 
    # [[0,0,0,0]
    # [1,1,1,1]
    # [2,2,2,2]
    # [3,3,3,3]]
    # 
    # og så bliver elementerne bare ganget med hinanden *
    return c

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
