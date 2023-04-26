#!/usr/bin/env python3

def merge(L1, L2):
    L = [] #the merged list
    x = 0 #index for L1
    y = 0 #index for L2
    while x < len(L1) and y < len(L2):
        if L1[x] < L2[y]:
            L.append(L1[x])
            x += 1
        else:
            L.append(L2[y])
            y += 1

    L.extend(L1[x:])
    L.extend(L2[y:])
    return L

def main():
    L1 = [1,5,6,11,13,21,59, 101, 117]
    L2 = [-42,0,3,4,9,10,15,22,509]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
