from util import Stack, Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    # this DTF has been modified to only return the last node of the graph, which should be the earliest ancestor
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        path = []
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                # print(v)
                visited.add(v)
                path.append(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        return path[-1]


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    did_add_vert = set()
    for pair in ancestors:
        if pair[0] not in did_add_vert:
            graph.add_vertex(pair[0])
            did_add_vert.add(pair[0])
        if pair[1] not in did_add_vert:
            graph.add_vertex(pair[1])
            did_add_vert.add(pair[1])
        graph.add_edge(pair[1], pair[0])
    # build edges in reverse
    return graph.dft(starting_node)
    # track the longest path length and the earliest ancestor node
    # do a bfs from starting_node to each other node
    # if path is longer or path is the same length and node is smaller
    #    return the longest path length







test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 6))






# q = []
#     q.append(starting_node)
#     visited = set()
#     for p in ancestors:
#         q.append(starting_node)
#     print(q)


# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
#
# # island_counter(islands) # returns 4
#
# def island_counter(matrix):
#     visited = []
#     matrix_height = len(matrix)
#     matrix_width = len(matrix[0])
#     for i in range(matrix_height):
#         visited.append( [False]* matrix_width )
#
#     counter = 0
#
#     for x in range(matrix_height):
#         if not visited[y][x]:
#             if matrix[y][x] == 1:

