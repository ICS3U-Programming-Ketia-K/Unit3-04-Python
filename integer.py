#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Dec 12, 2021
# This program checks if the entered integer is positive, negative or just zero

def main():
    # this function tells if an integer is positive, negative or just zero

    # input
    # this function will let the user input an integer of their choice
    integer = int(input("Please enter an integer: "))
    print("")
    # process & output
    # this function will give an output if one of the statements is true
    if integer < 0:
        print("This number is a negative number")
    elif integer > 0:
        print("This number is a positive number")
    elif integer == 0:
        print("This number is just zero!")


if __name__ == "__main__":
    main()
