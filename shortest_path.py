
graph = { 'u' : {'v':2, 'x':1, 'w':5 },
          'v' : {'u':2, 'x':2, 'w':3 },
          'x' : {'u':1, 'v':2, 'w':3, 'y':1 },
          'w' : {'u':5, 'v':3, 'x':3, 'y':1, 'z':5 },
          'y' : {'x':1, 'w':1, 'z':2 },
          'z' : {'w':5, 'y':2 }
          }

source = 'u'

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
    known_nodes.add(min_node)
    unknown_min_node_neighbors = {node for node in graph[min_node] } - known_nodes

    for node in unknown_min_node_neighbors:
        D[node] = min( D[node], (D[min_node][0] + graph[min_node][node], min_node) , key = lambda k: k[0]  )

# getting the paths

paths = { node:[] for node in nodes} # { node : [(source*, node1, node2 ... ,*node*] } (both source and node are omitted)

for node in nodes - {source}:
    previous = D[node][1]
    while previous != source:
        paths[node].append(previous)
        previous = D[previous][1]

# reveresing the paths order (to appear from source to destination)

for node in paths.keys():
    paths[node].reverse()
