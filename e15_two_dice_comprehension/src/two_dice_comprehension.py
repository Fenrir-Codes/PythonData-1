#!/usr/bin/env python3

def main():
    s=[(i, e) for i in range(1, 7) for e in range(1, 7) if i + e == 5]
    for i in s:
        print(i)
        
if __name__ == "__main__":
    main()
