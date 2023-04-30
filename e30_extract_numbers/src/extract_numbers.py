#!/usr/bin/env python3

def extract_numbers(s):
    words = s.split()
    numbers = []
    for word in words:
        try:
            num = int(word)
        except ValueError:
            try:
                num = float(word)
            except ValueError:
                continue
        numbers.append(num)
    return numbers


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
