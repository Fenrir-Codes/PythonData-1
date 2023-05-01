#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    filepath = r"C:\Users\Tec\Desktop\GhRep\Python-og-DataAnalyse_Oliver\excercises\part03\e05_correlation\src\iris.csv"
    return pd.read_csv(filepath).drop('species', axis=1).values

def lengths():
    data = load().T
    corr, p = scipy.stats.pearsonr(data[0], data[2])
    return corr

def correlations():
    data = load()
    R = np.corrcoef(data.T)
    return R

def main():
    print(lengths())
    print(correlations())
    # 123

if __name__ == "__main__":
    main()
