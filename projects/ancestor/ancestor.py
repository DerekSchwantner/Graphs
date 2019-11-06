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

    # build edges in reverse
    for pair in ancestors:
        graph.add_edge(pair[0], pair[1])
    print(graph.vertices)
    # print(did_add_vert)
    # track the longest path length and the earliest ancestor node
    # do a bfs from starting_node to each other node
    # if path is longer or path is the same length and node is smaller
    #    return the longest path length







test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 2))
earliest_ancestor(test_ancestors, 1)






# q = []
#     q.append(starting_node)
#     visited = set()
#     for p in ancestors:
#         q.append(starting_node)
#     print(q)