#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    List = []
    pattern = r"\s+(\d+)\s+([JFMAMJJASOND][a-z]+)\s+(\d{1,2})\s+(\d+):(\d+)\s(.+)"
    with open(filename, 'r') as f:
        for line in f:
            rec = re.findall(pattern, line, re.MULTILINE)
            List.append(rec)
    return List

def main():
    print(file_listing("e22_file_listing/src/listing.txt")) #H:\GitHub repositories\PythonData-H4\e22_file_listing\src

if __name__ == "__main__":
    main()
