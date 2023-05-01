#!/usr/bin/env python3
import pandas as pd


def read_series():
    ds = pd.Series()
    while True:
        inddata = input("Skriv index og værdi sep af whitespace: ")
        if inddata == '':
            break
        idx, val = inddata.split()
        ds[idx] = val
    return ds

def main():
    print(read_series())

if __name__ == "__main__":
    main()
