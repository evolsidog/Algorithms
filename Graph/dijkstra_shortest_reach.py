#!/bin/python3

# Solution to test cases for Dijkstra: Shortest Reach 2 problem in Hackerrank: https://www.hackerrank.com/challenges/dijkstrashortreach/problem

import math
import os
import random
import re
import sys
from collections import defaultdict
from queue import PriorityQueue


# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    
    # Traveled vertex
    traveled_vertex = []
    
    # Initialize distances to vertices
    min_distances = [float('inf') for i in range(n+1)]
    min_distances[s] = 0 # Start vertex has distance 0 to be the first chosen
        
    # Adyacent nodes
    marked_nodes = PriorityQueue()
    marked_nodes.put((min_distances[s], s)) # First node to travel is the start node
                
    while not marked_nodes.empty():
        # Get node marked with lowest distance
        current_min_distance, current_vertex = marked_nodes.get()
        if current_vertex not in traveled_vertex:
            # Check distances from current node
            for adyacent, distance in edges[current_vertex].items():
                if current_min_distance + distance < min_distances[adyacent]:
                    # Update min distances
                    min_distances[adyacent] = current_min_distance + distance
                    # Add modified nodes to marked queue if not traveled yet
                    if adyacent not in traveled_vertex:
                        marked_nodes.put((min_distances[adyacent], adyacent))
            
            # Marked node as fully visited
            traveled_vertex.append(current_vertex)
    
    # Remove empty zero position
    del min_distances[0]
    # Remove start vertex distance 0
    del min_distances[s-1]
    # Unreachable nodes are marked as -1
    print(min_distances)
    return [-1 if elem==float('inf') else elem for elem in min_distances]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = defaultdict(dict)
        for _ in range(m):
            edge = list(map(int, input().rstrip().split()))
            # Get lowest value from same edge
            if edge[1] in edges[edge[0]]:
                if edges[edge[0]][edge[1]] > edge[2]:
                    edges[edge[0]][edge[1]] = edge[2]
            else:
                edges[edge[0]][edge[1]] = edge[2]
                
            if edge[0] in edges[edge[1]]:
                if edges[edge[1]][edge[0]] > edge[2]:
                    edges[edge[1]][edge[0]] = edge[2]
            else:
                edges[edge[1]][edge[0]] = edge[2]

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
