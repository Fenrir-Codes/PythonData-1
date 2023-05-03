#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    filepath = r"H:\GitHub repositories\PythonData\øvelser\e59_subsetting_by_positions\src\UK-top40-1964-1-2.tsv"
    df = pd.read_csv(filepath, sep="\t")
    df = df.iloc[0:10, 2:4]
    return df

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()
