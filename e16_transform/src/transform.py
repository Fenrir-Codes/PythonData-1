#!/usr/bin/env python3

def transform(s1, s2):
    def calculate(L):
        result = int(L[0]) * int(L[1])
        return result
    zList = list(zip(s1.split(), s2.split()))
    return list(map(calculate, zList))
    

def main():
    print(transform("1 5 3", "2 6 -1"))
    #1*2 =2 , 5*6=30, 3*-1=-3

if __name__ == "__main__":
    main()
