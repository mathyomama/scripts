#!/usr/bin/env python


import sys
import re
import copy
import string


class SquareMystery():

    def __init__(self, template):
        if SquareMystery.is_template(template):
            self.template = template
            self.length = len(self.template)
        else:
            raise Exception

    @staticmethod
    def is_template(template):
        for i in template:
            if not (i.isdigit() or i == '.'):
                return False
        return True

    def compare_to_template(self, value, depth):
        smallTemplate = self.template[self.length - depth:self.length]
        for a, b in zip(value, smallTemplate):
            if b != '.' and a != b:
                return False
        return True

    def solve(self, possibleValues, depth):
        newPossibleValues = []
        for digits in possibleValues: # digits should be a list of strings which fit the criteria
            limit = len(digits)
            for digit in string.digits:
                testString = digit + digits
                value = str(int(testString)**2 % 10**depth)
                while(len(value) != depth):
                    value = '0' + value
                if self.compare_to_template(value, depth):
                    newPossibleValues.append(testString)
        return newPossibleValues

def main():
    euler206 = SquareMystery("1.2.3.4.5.6.7.8.9.0")
    possibleValues = ["30", "70"]
    depth = 3
    while depth < 11:
        possibleValues = euler206.solve(possibleValues, depth)
        depth += 1
    pat1 = re.compile(r"1\d{9}")
    pat2 = re.compile(r"1\d2\d3\d4\d5\d6\d7\d8\d9\d0")
    for i in possibleValues:
        if pat1.match(i) and pat2.match(str(int(i)**2)):
            print(i)

if __name__ == "__main__":
    sys.exit(main())
