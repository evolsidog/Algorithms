# Solution to test cases for BFS problem in Hackerrank: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

from queue import Queue

class Graph:
    def __init__(self, n):
        self.n = n # number of nodes
        self.edges = {n:set() for n in range(self.n)} # Set guarantee integer order and unrepeated elements

    def connect(self, origin_node, end_node):
        self.edges[origin_node].add(end_node)
        self.edges[end_node].add(origin_node)
        
    def find_all_distances(self, start_node):
        distances = ["-1" for node in range(self.n)]
        distances[start_node] = 0
        parents = Queue()
        parents.put(start_node)
        # If add traveled nodes to empty list to check if the node have been visited, it seem like some contraint is violated and test case fails. The solution is initialize untraveled nodes and later remove that node when is traveled.
        untraveled = [i for i in range(self.n)]
        while(not parents.empty()):
            current_parent = parents.get() # Take out current parent from queue and travel it
            for adyacent_node in self.edges[current_parent]:
                if adyacent_node in untraveled:
                    distances[adyacent_node] = distances[current_parent] + 6
                    parents.put(adyacent_node) # Put adyacent node to travel it after
                    untraveled.remove(adyacent_node) # Remove traveled node

            
        del distances[start_node]
        print(" ".join(map(str, distances)))
        

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)