#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    loop = bool = True
    while loop:
        value = input("Choose a shape (triangle, rectangle, circle): ")
        if(value == "triangle"):
            base = input("Give base of the triangle: ")
            height = input("Give height of the triangle: ")
            area = (float(base) * float(height) / 2)
            print(f"The area is {area}")
        elif(value == "rectangle"):
            width = input("Give width of the rectangle: ")
            height = input("Give height of the rectangle: ")
            area = float(width) * float(height)
            print(f"The area is {area}")
        elif(value == "circle"):
            radius = input("Give radius of the circle: ")
            area = float(radius)**2 * 3.14159265
            print(f"The area is {area}")
        elif(value ==""):
            loop = False
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
