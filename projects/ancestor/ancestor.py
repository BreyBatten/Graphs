# 3 steps to solve almost any graphs problem
## Describe problem in terms of graphs
### Nodes: people
### Edges: if nodes are parent/child

## Build our graph
### Build graph class
### Don't write adjacency list or matrix, just a getNeighbors function

## Choose a graph algorithm
### Traversal or search? => Traversal because we aren't looking for specific node
### Breadth first or Depth first? => Because we are traversing, it doesn't really matter which 
#### We are using DFT for this problem

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add(parent)

    def getNeighbors(self, child):
        return self.nodes[child]

class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, item):
        self.storage.append(item)

    def size(self):
        return len(self.storage)

def dft():
    s = Stack()
    s.push((starting_node, 0))
    visited = set()
    visited_pairs = set()

    while s.size() > 0:
        current_pair = s.pop()
        visited_pairs.add(current_pair)
        current_node = current_pair[0]
        current_distance = current_pair[1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.getNeighbors(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                s.push((parent, parent_distance))

    longest_distance = 0
    aged_one = -1

    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]
        if distance > longest_distance:
            longest_distance = distance
            aged_one = node
    return aged_one

def earliest_ancestor(ancestors, starting_node):
    # build graph
    graph = Graph()
    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)

    # run dft
    aged_one = dft(graph, starting_node)

    # choose longest path (most distant ancestor)
    ## run dft but track each path, then choose the longest path
    ## run dft but add each node as a tuple (node, distance)
    return aged_one
