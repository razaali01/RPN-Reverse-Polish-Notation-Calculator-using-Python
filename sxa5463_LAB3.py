# Name: Syed Ali
# NetID: 1001725463
# Date Turned In: 4/7/2022
# Python Version 3.10

import os


# function to calculate values in RPN
def RPNCalculator(RPN, operators):
    # making a stack
    stack = []

    # separating the string
    SplitRPN = RPN.split()

    for x in SplitRPN:
        # check if x is part of the operators list
        if x in operators:

            val2 = stack.pop()

            val1 = stack.pop()

            # check is operator is addition
            if x == '+':
                results = val1 + val2
            # check is operator is subtraction
            elif x == '-':
                results = val1 - val2
            # check is operator is multiplication
            elif x == '*':
                results = val1 * val2
            # check is operator is division
            elif x == '/':
                results = val1 / val2

            # store results in the stack
            stack.append(results)
        else:
            # if not an operator then it is a number so push it
            # back to the stack
            stack.append(float(x))

    # return the result
    return stack.pop()


# opening file to read
Fileinput = open('input_RPN.txt', 'r')

# saving lines in the file
StuffInFile = Fileinput.readlines()

# stating which operators are allowed
operators = ["+", "-", "*", "/"]

for x in StuffInFile:
    RPN = x
    print(RPNCalculator(RPN, operators))

# closing file
Fileinput.close()
