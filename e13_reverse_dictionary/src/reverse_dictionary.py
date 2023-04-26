#!/usr/bin/env python3

def reverse_dictionary(d):
    rev = {}
    for i in d:
        for e in range(len(d[i])):
            if d[i][e] in rev:
                rev[d[i][e]].append(i)
            else:
                rev[d[i][e]] = [i]
    return rev

def main():
    d = {'move': ['liikutta'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
