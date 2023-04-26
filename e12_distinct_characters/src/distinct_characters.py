#!/usr/bin/env python3

def distinct_characters(L):
    dist = {}  #array thing
    for i in L: #for loop looping L list
        dist[i]=len(set(i)) #dist[value] set[value length in number]
    return dist

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
