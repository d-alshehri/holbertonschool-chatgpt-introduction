#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number using recursion.
# The factorial of a number n is the product of all positive integers less than or equal to n.
# For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

# Parameters:
# - n (int): The number for which the factorial is to be calculated. It must be a non-negative integer.
#
# Returns:
# - (int): The factorial of the number n. If n is 0, it returns 1 (since 0! = 1 by definition).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the input number from command line arguments
f = factorial(int(sys.argv[1]))

# Print the result (factorial of the input number)
print(f)
