#!/usr/bin/env python3

import pandas as pd
#import os

def main():
    filepath = r"H:\GitHub repositories\PythonData\øvelser\e54_municipal_information\src\municipal.tsv"
    df = pd.read_csv(filepath, sep="\t")
    
    print(f"Shape: {df.shape[0]},{df.shape[1]}")
    print("Columns:")
    for c in df.columns:
        print(c)


if __name__ == "__main__":
    main()
