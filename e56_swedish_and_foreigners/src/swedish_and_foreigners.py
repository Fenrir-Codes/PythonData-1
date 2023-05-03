#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    filepath = r"H:\GitHub repositories\PythonData\øvelser\e56_swedish_and_foreigners\src\municipal.tsv"
    muni = pd.read_csv(filepath, sep="\t", index_col="Region 2018")
    
    muni = muni["Akaa":"Äänekoski"]
    
    muni = muni[
        (muni["Share of Swedish-speakers of the population, %"] > 5)
        &
        (muni["Share of foreign citizens of the population, %"] > 5)
    ]
    
    res = muni[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    
    return res
def main():
    print(swedish_and_foreigners().head())
    return

if __name__ == "__main__":
    main()
