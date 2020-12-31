#!/bin/python3

# Solution to test cases for Swap Nodes [Algo] problem in Hackerrank: https://www.hackerrank.com/challenges/swap-nodes-algo/problem

import os
import sys
from queue import Queue

# Another way to avoid recursion is store in a list all methods calls with her parameters and later loop it to invoke it and store the results.
sys.setrecursionlimit(15000) # Change limit recusrion for test cases 10 and 11. 


class Node:
    def __init__(self, depth, value, left=None, right=None):
        self.depth = depth
        self.value = value
        self.left = left
        self.right = right

        
class BinaryTree:
    def __init__(self):
        self.tree = None
    
    def build(self, nodes):
        # Ensure that tree is not empty
        if nodes:
            self.tree = Node(depth=0, value=1, left=None, right=None) # Root node
            not_visited_nodes = Queue()
            not_visited_nodes.put(self.tree) 
            for index in nodes:
                current_parent = not_visited_nodes.get()
                # Left child
                if index[0] != -1:
                    current_parent.left = Node(depth=current_parent.depth+1, value=index[0], left=None, right=None)
                    not_visited_nodes.put(current_parent.left)
                # Right child
                if index[1] != -1:
                    current_parent.right = Node(depth=current_parent.depth+1, value=index[1], left=None, right=None)
                    not_visited_nodes.put(current_parent.right)        
    
    def travel_in_order_with_swaps(self, start_node, depth):
        visited = []
        # Ensure tree not is empty
        if start_node:
            # If children depth is multiple of depth, swap right and left child
            if (start_node.depth + 1) % depth == 0:
                start_node.left, start_node.right = start_node.right, start_node.left
            
            # Append left node
            if start_node.left:
                visited += self.travel_in_order_with_swaps(start_node=start_node.left, depth=depth)
            
            # Append parent
            visited.append(start_node.value)
            
            # Append right node
            if start_node.right:
                visited += self.travel_in_order_with_swaps(start_node=start_node.right, depth=depth)
        
        return visited    
        
        
#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    travel_result = []
    binary_tree = BinaryTree()
    binary_tree.build(nodes=indexes)
    for query in queries:
        travel_result.append(binary_tree.travel_in_order_with_swaps(start_node=binary_tree.tree, depth=query))

    return travel_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
