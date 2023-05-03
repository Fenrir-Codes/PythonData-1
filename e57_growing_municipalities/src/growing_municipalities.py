#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    nmuni = df.shape[0]
    print(nmuni)
    nGrowMuni = df[df['Population change from the previous year, %']>0].shape[0]
    print(nGrowMuni)
    return nGrowMuni / nmuni

def main():
    filepath = r"H:\GitHub repositories\PythonData\øvelser\e57_growing_municipalities\src\municipal.tsv"
    muni = pd.read_csv(filepath, sep="\t", index_col="Region 2018")['Akaa':'Äänekoski']
    print(f"Proportion of growing municipalities: {growing_municipalities(muni) *100 :.1f}%")

if __name__ == "__main__":
    main()
