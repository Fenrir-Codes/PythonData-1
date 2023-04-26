#!/usr/bin/env python3

def detect_ranges(L):
    L = sorted(L)
    returningList = [] # [2,(4,9),10,(12,14)]
    
    i = 0
    start = None

    while i < len(L) -1:
        if L[i + 1] == L[i] + 1:
            if start is None:
                start = i
        else:
            if start is None:
                returningList.append(L[i])
            else:
                returningList.append((L[start], L[i] + 1))
                start = None
        i += 1
    if start is None:
        returningList.append(L[i])
    else:
        returningList.append((L[start], L[i] + 1))
    return returningList

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
