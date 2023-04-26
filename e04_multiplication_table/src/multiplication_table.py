#!/usr/bin/env python3


def main():
    for i in range(1,11):
        for e in range(1,11):
            #print(i, "*", e ,"=", i*e)
            #print("%i times %i is aqual to %i" % (i,e,i*e))
            print(f"{i*e:4d}", end="\t")
        print()        
        

if __name__ == "__main__":
    main()
