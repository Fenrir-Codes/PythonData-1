#!/usr/bin/env python3
def triple(num: int):
    return num*3

def square(num: int):
    return num*num

def main():
    for i in range(1,11):
        triplevalue = triple(i)
        squarevalue = square(i)
        if(triplevalue < squarevalue):
            break
        else:
            print("Triple(" +str(i) + ")==" + str(triplevalue), "Square("+ str(i) + ")=="+ str(squarevalue))

if __name__ == "__main__":
    main()
