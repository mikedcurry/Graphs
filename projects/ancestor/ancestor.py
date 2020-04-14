#  from util import Stack, Queue
 
 # Easier to visualize what I need to do...
'''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
General attack will be create a graph and do a BFS

'''

# Queue class copied and pasted from util
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Re-create bare-bones Graph class
class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # if it doesn't already exist add vertex to vertices
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        # else:
        #     raise IndexError('vertex already exists')

    # add --> ***DIRECTED*** <-- edges (that really screwed me up...)
    def add_edges(self, v1, v2):
        # make sure vertices exist, then add the DIRECTED edge
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('an input vertex does not exist')
    
    
def earliest_ancestor(ancestors, starting_node):
    #instatiate graph
    graph = Graph()

    # add all the vertices and edges to graph
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # add all DIRECTED edges to graph IN REVERSE --> to swim upstream to parents from kids
        graph.add_edges(pair[1], pair[0])

    # BFS starts here, with adding the starting node to the queue
    q = Queue()
    q.enqueue([starting_node])

    # set initial conditions - overwritten if any pair exist
    max_path_length = 1
    earliest_ancestor = -1

    # main BFS loop, with extra stuff to find longest path / earliest ancestor
    while q.size():
        path = q.dequeue()
        v = path[-1]

        # if we find a longer path, then update earliest ancester, account for tie
        if (len(path) > max_path_length) or (len(path) >= max_path_length and v < earliest_ancestor):
            # update earliest ancestor
            earliest_ancestor = v
            #update longest path
            max_path_length = len(path)


        for friend in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(friend)
            q.enqueue(path_copy)
        
    return earliest_ancestor


# Prior attempt, before watching video...

# def earliest_ancestor(ancestors, starting_node):
#     lineage = []
#     stack = []
#     stack = stack + [starting_node]

#     while len(stack): 
#         roots = stack.pop(-1)

#         no_roots = True
#         for pair in lineage:
#             if pair[1] == lineage[-1]:
#                 stack.append([*roots, pair[0]])
#                 no_roots = False

        
#         break

#     return


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# earliest_ancestor(test_ancestors, 1)
# earliest_ancestor(test_ancestors, 2)