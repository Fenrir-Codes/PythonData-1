#!/usr/bin/env python3

import pandas as pd

def create_series(L1, L2):
    ds1 = pd.Series(L1, index=list("abc"), dtype='object')
    ds2 = pd.Series(L2, index=list("abc"), dtype='object')
    return (ds1, ds2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del(s2['b'])
    return (s1, s2)
    
def main():
    ds1, ds2 = create_series(['hest', 'hund', 'kat'], ['ko', 'kanin', 'gris'])
    print(f"ds1:\n", ds1)
    print(f"ds2:\n", ds2)
    
    ds1, ds2 = modify_series(ds1, ds2)
    print(f"ds1:\n", ds1)
    print(f"ds2:\n", ds2)
    
    
if __name__ == "__main__":
    main()
