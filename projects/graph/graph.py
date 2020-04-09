"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        v1_edges_set = self.vertices[v1]
        v1_edges_set.add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create empty queue
        q = Queue()
        # enqueue the starting_vertex
        q.enqueue(starting_vertex)
        # create a set to create vertices we have visited
        visited = set()
        # while queue isn't empty
        while q.size() != 0:
        # dequeue, this is our current_node
            current_node = q.dequeue()
        # if we haven't visited it yet
            if current_node not in visited:
        # mark as visited
                visited.add(current_node)
        # get it's neighbors
                neighbors = self.get_neighbors(current_node)
        # enqueue each neighbor
                for neighbor in neighbors:
                    q.enqueue(neighbor)
        # return visited
        return visited


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack
        s = Stack()
        # push the starting_vertex onto stack
        s.push(starting_vertex)
        # create visited set
        visited = set()
        # while stack is not empty
        while s.size() > 0:
        # pop off top of stack, this is our current_node
            current_node = s.pop()
        # if it hasn't been visited:
            if current_node not in visited:
        # mark as visited
                visited.add(current_node)
        # get it's neighbors
                neighbors = self.get_neighbors(current_node)
        # add each neighbor to top of stack
                for neighbor in neighbors:
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        def dft_r(vertex):
            visited.add(vertex)
            for node in self.vertices[vertex]:
                if node not in visited:
                    dft_r(node)

        dft_r(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() is not None:
            current_path = q.dequeue()
            current_node = current_path[-1]
            visited.add(current_node)

            if current_node == destination_vertex:
                return current_path
            
            for node in self.vertices[current_node]:
                if node not in visited:
                    path_copy = current_path[:]
                    path_copy.append(node)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() is not None:
            current_path = s.pop()
            current_node = current_path[-1]
            visited.add(current_node)

            if current_node == destination_vertex:
                return current_path
            for node in self.vertices[current_node]:
                if node not in visited:
                    path_copy = current_path[:]
                    path_copy.append(node)
                    s.push(path_copy)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        def dfs_r(path):
            current_node = path[-1]
            visited.add(current_node)
            if current_node == destination_vertex:
                return path
            for node in self.vertices[current_node]:
                if node not in visited:
                    path_copy = path[:]
                    path_copy.append(node)
                    s.push(path_copy)
            return dfs_r(s.pop())

        return dfs_r(s.pop())
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
