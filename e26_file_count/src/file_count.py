#!/usr/bin/env python3

import sys

def file_count(filename):
    linecount = 0
    wordcount = 0
    charactercount = 0
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1   
            wordcount += len(line.split())
            charactercount += len(line)
    return (linecount, wordcount, charactercount)

def main():
    for filename in sys.argv[1:]:
        out = file_count(filename)
        print(*out, filename, sep="\t")

if __name__ == "__main__":
    main()