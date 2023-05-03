#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    filepath = r"H:\GitHub repositories\PythonData\øvelser\e60_snow_depth\src\kumpula-weather-2017.csv"
    wh = pd.read_csv(filepath,)
    maxSnow = wh['Snow depth (cm)'].max()
    return maxSnow

def main():
    print(f"Max snow depth: {snow_depth()}")

if __name__ == "__main__":
    main()
