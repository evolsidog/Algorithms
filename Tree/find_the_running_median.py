#!/bin/python3

# # Solution to test cases for Find the running median problem in Hackerrank: https://www.hackerrank.com/challenges/find-the-running-median/problem

import os
import sys
import heapq
        
#
# Complete the runningMedian function below.
#
def runningMedian(a):
    #
    # Write your code here.
    #
    
    # heapq always create a min_heap
    lowers = []  # We store negative numbers as positive, since heapq always create a min_heap. Root is the highest negative number.
    highers = [] # We store positive number. Root is the smallest positive number.
    medians = []
    for elem in a:
        # Add elem
        if not lowers or elem < -lowers[0]:
            heapq.heappush(lowers, -elem)
        else:
            heapq.heappush(highers,num)
        # Check if is necessary balance heaps
        if len(highers) - len(lowers) >= 2:
            heapq.heappush(lowers, -heapq.heappop(highers))
        elif len(lowers) - len(highers) >=2:
            heapq.heappush(highers, -heapq.heappop(lowers))
        # Calculate median
        if len(highers) == len(lowers):
            medians.append((-lowers[0] + highers[0])/2)
        elif len(highers) > len(lowers):
            medians.append(highers[0])
        else:
            medians.append(lowers[0])
    
    return medians

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
