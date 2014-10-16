def shortest_path(graph,source, destination = None):
    '''
    Takes a graph, a source node, a destination node and returns
    the shortest path from the source to the destination node.

    All nodes are represented by strings.
    The graph takes the shape:
    graph = { node : { adjacent nodes and the costs of direct edges leadin to them}, another node : { ... }, ... }

    Example:
    
    graph = { 'u' : {'v':2, 'x':1, 'w':5 },
                'v' : {'u':2, 'x':2, 'w':3 },
                'x' : {'u':1, 'v':2, 'w':3, 'y':1 },
                'w' : {'u':5, 'v':3, 'x':3, 'y':1, 'z':5 },
                'y' : {'x':1, 'w':1, 'z':2 },
                'z' : {'w':5, 'y':2 }
                }

    If destination node is provided, the function returns the path
    from the source node the destination node and the cost of the past.
    If not provided, the function returns the paths and costs to
    all nodes in the graph.
    '''

    nodes = set(graph.keys())

    # Initialization
    known_nodes = {source} # nodes which least destinations are known 

    D = {} # { node : (least cost, previous node in the path), another node : (.., ..), ... }

    source_neighbors = {node[0] for node in graph[source]}
    for node in nodes:
        if node in source_neighbors:
            D[node] = (graph[source][node],source)
        else:
            D[node] = (float('inf'), '-')

    # loop
    while nodes != known_nodes:
        min_node = min(nodes - known_nodes,key= lambda node: D[node][0] )
        if min_node == destination: # if destination is provided
            return (form_path(D, nodes, source, destination), D[destination][0]) # returns (path,cost)
        known_nodes.add(min_node)
        unknown_min_node_neighbors = {node for node in graph[min_node] } - known_nodes

        for node in unknown_min_node_neighbors:
            D[node] = min( D[node], (D[min_node][0] + graph[min_node][node], min_node) , key = lambda k: k[0]  )

    # if destination is not provided, return all paths

    paths = {} #paths = { node : ([source*, node1, node2 ... ,*node*], cost), ... } (both source and node are omitted)
    
    for node in nodes - {source}:
        paths[node] = (form_path(D,nodes,source,node), D[node][0])
    return paths

# helper function; form source -> destination path
def form_path(D, nodes, source,destination):
    path = []
    previous = D[destination][1]
    while previous != source:
        path.append(previous)
        previous = D[previous][1]
    path.reverse()
    return path
    
# Example

graph = { 'u' : {'v':2, 'x':1, 'w':5 },
                'v' : {'u':2, 'x':2, 'w':3 },
                'x' : {'u':1, 'v':2, 'w':3, 'y':1 },
                'w' : {'u':5, 'v':3, 'x':3, 'y':1, 'z':5 },
                'y' : {'x':1, 'w':1, 'z':2 },
                'z' : {'w':5, 'y':2 }
                }
source = 'u'
dest = 'z'
# Path and cost from u to z
(path, cost) = shortest_path(graph, source, dest)
print(*path,sep='->')
# Paths and costs from u to all of the other nodes
paths = shortest_path(graph, source)
print(*paths.items(), sep = '\n')
