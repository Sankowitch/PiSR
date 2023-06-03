#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

listOfNumbers = []

"""asking the user (on the standard input) for a floating point number x."""
x = float(input("Enter a floating point number: "))

"""reading numbers from the input file and adding x to each number"""
with open(sys.argv[1],'r') as first_file:
    for number in first_file:
        listOfNumbers.append(float(number) + x)

"""Printing the results on the screen
AND also writing them into the given output file, one per line"""
with open(sys.argv[2], 'w') as second_file:
    for number in listOfNumbers:
        second_file.write("{:.3f}".format(number)+'\n') 
        print("{:.3f}".format(number))
