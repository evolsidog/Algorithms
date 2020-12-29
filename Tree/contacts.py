#!/bin/python3

# Solution to test cases for Contacts problem in Hackerrank: https://www.hackerrank.com/challenges/contacts/problem

import os
import sys
from queue import Queue
    

class TrieNode:
    
    def __init__(self):
        # It is guaranteed that  and  contain lowercase English letters only
        # 26 positions: a b c d e f g h i j k l m n o p q r s t u v w x y z
        self.children = [None]*26
        self.is_leaf = False # Mark if the node is a complete word
        self.n_children = 0
        
    
    def _get_index(self, character):
        # Return index position by character
        return ord(character)-ord("a")
    
    def add(self, name):
        current_node = self
        for character in name:
            index = self._get_index(character)
            if not current_node.children[index]:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]
            current_node.n_children += 1
        current_node.is_leaf = True
    
    def find(self, partial):
        current_node = self
        for character in partial:
            index = self._get_index(character)
            if not current_node.children[index]:
                return 0
            else:
                current_node = current_node.children[index]
        return current_node.n_children
        
#
# Complete the contacts function below.
#
def contacts(queries):
    #
    # Write your code here.
    #
    
    contact_book = TrieNode()
    partials = []
    for query in queries:
        operation = query[0]
        param = query [1]
        if operation == "add":
            contact_book.add(param)
        elif operation == "find":
            partials.append(contact_book.find(param))
            # partials.append(sum([1 for c in contact_book if c.startswith(param)]))
    
    return partials        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
