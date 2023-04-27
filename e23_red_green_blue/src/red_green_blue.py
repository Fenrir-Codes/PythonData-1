#!/usr/bin/env python3

import re #The code first imports the regular expressions module re.

#The red_green_blue function takes a filename as an argument (defaulting to "src/rgb.txt"). 
# It initializes an empty list L and a regular expression pattern pattern that will be used to search for lines containing color information in the file.

#The function opens the file specified by filename using a with statement, which ensures that the file is properly 
# closed when the block of code inside the with statement is executed.

#The function then loops over each line in the file and uses the regular expression search method to find matches for the pattern in each line.
#  If a match is found, it extracts the color information using the groups method and joins the values with a tab separator. 
# This joined string is then appended to the L list.

#Finally, the function returns the L list containing all the color information extracted from the file.

#The main function is defined next. It simply calls the red_green_blue function with the path to the "src/rgb.txt" file as an argument and prints the resulting list.

#The if __name__ == "__main__": statement at the end of the code ensures that the main function is only executed 
# if the script is run directly (as opposed to being imported as a module).

def red_green_blue(filename="src/rgb.txt"):
    L = []
    pattern = "(\d+)\s+(\d+)\s+(\d+)\s+(.+)"
    with open(filename, 'r') as f:        
        for line in f:
            mo = re.search(pattern, line) # search each line
            if mo:
                colorInfo = mo.groups()
                # print(colorInfo) # List of colorvalues
                r = "\t".join(colorInfo)
                L.append(r)              
    return L

# with lambda:
#red_green_blue = lambda filename="src/rgb.txt": [ "\t".join(mo.groups()) for mo in (re.search("(\d+)\s+(\d+)\s+(\d+)\s+(.+)", line) for line in open(filename)) if mo ]



def main():
    print(red_green_blue(r"e23_red_green_blue\src\rgb.txt"))

if __name__ == "__main__":
    main()
