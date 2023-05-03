#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    filepath = r"H:\GitHub repositories\PythonData\øvelser\e58_subsetting_with_loc\src\municipal.tsv"
    muni = pd.read_csv(filepath, sep="\t", index_col="Region 2018")
    res = muni.loc['Akaa':'Äänekoski', ["Population", 
                                        "Share of Swedish-speakers of the population, %", 
                                        "Share of foreign citizens of the population, %"]]
    
    return res

def main():
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()