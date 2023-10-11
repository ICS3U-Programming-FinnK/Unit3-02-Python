#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: October 11th, 2023
# this program checks if the number the user guessed is correct.
import constants


def main():
    # the user inputs the number from 0 to 9
    number = int(input("Enter a number between 0 to 9: "))
    print("")

    # the terminal will check of the correct number is wrong
    if number < constants.CORRECT_NUMBER:
        print("the number is incorrect, please try again!")


if __name__ == "__main__":
    main()
