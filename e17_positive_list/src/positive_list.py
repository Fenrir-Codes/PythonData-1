#!/usr/bin/env python3

def positive_list(L):
    def ifPositive(x):
        return x > 0 #find numbers if bigger than 0
    return list(filter(ifPositive, L))

def main():
    print(positive_list([2, -2, 0, 1, -7])) #list

if __name__ == "__main__":
    main()
