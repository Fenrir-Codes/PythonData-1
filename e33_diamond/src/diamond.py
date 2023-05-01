#!/usr/bin/env python3

import numpy as np

def diamond(n):
    d = np.eye(n, dtype=int)
    d1 = d[:,1:][:,::-1]
    d2 = np.concatenate((d1,d), axis=1)
    d3 = d2[:-1, :][::-1, :]
    d4 = np.concatenate((d2, d3), axis=0)
    return d4

def main():
    print(diamond(3))
    print(diamond(5))
    print(diamond(8))

if __name__ == "__main__":
    main()
