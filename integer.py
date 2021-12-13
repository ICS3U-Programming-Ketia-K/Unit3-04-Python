#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Dec 12, 2021
# This program checks if the entered integer is positive, negative or just zero

def main():
    # this function tells if an integer is positive, negative or just zero
    # Get an input from the user of a integer of their choice
    integer = int(input("Please enter an integer: "))
    print("")

    # The program receives the input
    # it will then figure out if the integer is positive, negative or zero
    # Then, it will give an output of one of the statements that is true
    if integer < 0:
        print("This number is a negative number")
    elif integer > 0:
        print("This number is a positive number")
    else:
        print("This number is just zero!")


if __name__ == "__main__":
    main()
