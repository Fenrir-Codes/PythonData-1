#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    ds = pd.Series(s.index, index=s.values)
    return ds

def main():
    ds1 = pd.Series(['Bendt', 'Jan', 'Allan'], index=[2, 1, 3])
    print(inverse_series(ds1))
    lst = ['Jan', 'Bendt']
    lst1 = ['Allan', 'Jan']
    print(pd.Series([lst, lst1], index=[1,2]))

if __name__ == "__main__":
    main()
