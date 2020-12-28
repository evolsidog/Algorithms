#!/bin/python3

# Solution to test cases for balanced brackets problem in Hackerrank: https://www.hackerrank.com/challenges/balanced-brackets/problem

import math
import os
import random
import re
import sys
from queue import LifoQueue

start_brackets = ["{", "[", "("]
end_brackets = ["}", "]", ")"]

pair_brackets = {end:start for start, end in zip(start_brackets, end_brackets)}

# Complete the isBalanced function below.
def isBalanced(s):
    # Check length sequence is even to avoid malformed cases
    if len(s) % 2 != 0:
        return "NO"
    
    # Stack to store start brackets
    start_brackets_read = LifoQueue()
    for bracket in s:
        # Store start bracket
        if bracket in start_brackets:
            start_brackets_read.put(bracket)
        # Check stack has element, since doesn't raise exception.
        elif bracket in end_brackets:
            if start_brackets_read.empty() or start_brackets_read.get() != pair_brackets[bracket]:
                return "NO"
        else:
            return "NO"
    
    # Check all start brackets have been matched
    return "YES" if start_brackets_read.empty() else "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    print(pair_brackets)
    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
