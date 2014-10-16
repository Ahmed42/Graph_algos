Graph_algos
===========

Simple implementations of some graph algorithms. For educational purposes :)

Shortest Path:
--------------
### Dijkstra:
shortest_path in shortest_path.py implements Dijkstra's shortest path algorithm. A node is represented by a string. A graph is represented by a dictionary. The keys are the graph nodes and the value of each key is a dictionary that represents the neighboring nodes and the costs of the direct edges leading to them.

The function takes a graph, a source node and a destination node (optional argument). If the destination node is supplied, the function returns an ordered pair (list of nodes that form the path from the source to the destination, cost of the path). If the destination node is not supplied, the function returns the paths to all nodes in the graph from the source node and their costs in the form: ```{node : ([node1, node2, ... , nodeN], path cost) , another_node : ([...] ,... ), ... }```
