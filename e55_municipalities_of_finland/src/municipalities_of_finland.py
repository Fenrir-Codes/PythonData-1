#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    filepath = r"H:\GitHub repositories\PythonData\øvelser\e55_municipalities_of_finland\src\municipal.tsv"
    muni = pd.read_csv(filepath, sep="\t", index_col="Region 2018")
    muni = muni["Akaa": "Äänekoski"]
    return muni
    
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
