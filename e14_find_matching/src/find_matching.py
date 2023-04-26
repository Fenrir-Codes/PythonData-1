#!/usr/bin/env python3

def find_matching(L, pattern):
    returnThis = []
    for key, value in list(enumerate(L)):
        if pattern in value:
            returnThis.append(key)
    return returnThis


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))
    #returning the number of position where it could find "en" in the words
if __name__ == "__main__":
    main()
