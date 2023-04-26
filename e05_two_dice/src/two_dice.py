#!/usr/bin/env python3

def main():
    for i in range(1,7):
        for e in range(1,7):
                if(i + e == 5):
                 print("("+str(i)+ "," +str(e)+ ")")

if __name__ == "__main__":
    main()
