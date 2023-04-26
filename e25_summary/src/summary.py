#!/usr/bin/env python3

import sys
import math

def summary(filename):
    print(filename)
    with open(filename, 'r') as f:
        L = []
        for line in f:
            try:
                f = float(line)
                L.append(f)
            except ValueError:
                pass
        sm = sum(L)
        avg = sm / len(L)
        dif = 0
        for x in L:
            dif += (x - avg)**2
        stddiv = math.sqrt(dif / (len(L) - 1))
    return (sm, avg, stddiv)

def main():
    for filename in sys.argv[1:]:
        out = summary(filename)
        print(f"File: {filename} Sum: {out[0]:.6f} Average: {out[1]:.6f} Stddev: {out[2]:.6f}")
        

if __name__ == "__main__":
    main()