#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program uses a while loop to solve the power of ever number
#   up to the inputted number


def main():
    # this function uses a while loop to solve the power of ever number
    #   up to the inputted number

    # this is to keep track of how many times you go through the loop
    loop_counter = 0
    final = 0

    # input
    print("\n", end="")
    amount = input("Enter how many integers you want to add (+): ")

    # process & output
    try:
        amount_int = int(amount)
        print("\n", end="")

        if amount_int <= loop_counter:
            print("You did not enter a positive integer!")

        else:
            while loop_counter < amount_int:

                number = input("Enter a integer (+): ")
                number_int = int(number)

                final = final + number_int

                loop_counter = loop_counter + 1

            print("\nThe sum of all your integers is {0}.".format(final))

    except Exception:
        print("\nYou have entered an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
