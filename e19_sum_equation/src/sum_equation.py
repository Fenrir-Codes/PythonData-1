#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0: # if L length is 0 so it is null
        e = 0
    else:
        e = [str(i) for i in L] #or e = string i in List
    returning = " + ".join(e) #add a + sign between numbers
    return f"{returning} = {sum(L)}" #sum L



def main():
    print(sum_equation([1, 5, 7]))

if __name__ == "__main__":
    main()
