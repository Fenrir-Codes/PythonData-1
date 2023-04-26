#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    L = []
    pattern = "(\d+)\s+(\d+)\s+(\d+)\s+(.+)"
    with open(filename, 'r') as f:        
        for line in f:
            mo = re.search(pattern, line) # search each line
            if mo:
                colorInfo = mo.groups()
                # print(colorInfo) # List of colorvalues
                r = "\t".join(colorInfo)
                L.append(r)              
    return L


def main():
    print(red_green_blue(r"e23_red_green_blue\src\rgb.txt"))

if __name__ == "__main__":
    main()
