#!/usr/bin/env python3

import numpy as np
import pandas as pd

def cities():
    data = np.array([[643272,     715.48],
            [279044,     528.03],
            [231853,     689.59],
            [223027,     240.35],
            [201810,     3817.52]])
    cities = [
        "Helsinki", 
        "Espoo", 
        "Tampere", 
        "Vantaa", 
        "Oulu"
    ]
    
    column_names = ["Population", "Total area"]
    pop = [643272, 279044, 231853, 223027, 201810]
    ta = [715.48, 528.03, 689.59, 240.35, 3817.52]
    df = pd.DataFrame(data, columns=column_names, index=cities)
    return df
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
