# set of nodes
# set of edges in a dictionary; {(node, node): weight}
# the index of the source node
# This function follows Dijkstra's algorithm
# which returns the shortest distance from the source node
# to each node 
def dijkstra(nodes, edges, src_index):
    # initialize each path distance with temp values (inf)
    path_length = {v: float('inf') for v in nodes}
    path_length[src_index] = 0

    # initialize its adjacent nodes with
    # keys as its nodes and values as a subdictionary
    # made up of its corresponding nodes and weights
    adj_nodes = {v : {} for v in nodes}
    #  (node,node):weight in edges{}
    for (i, j), weights_ij in edges.items():
        adj_nodes[i][j] = weights_ij
        adj_nodes[j][i] = weights_ij

    # choose a temp node i with the smallest path length
    # mark it as permanent then update our shortest path for
    # every temp node j adjacent to i
    # until there are no more temp nodes left in the list
    temp_nodes = [v for v in nodes]
    while len(temp_nodes) > 0:
        #first find the temp node with the smallest path length i
        temp_path_lengths = {v: path_length[v] for v in temp_nodes}
        i = min(temp_path_lengths, key=temp_path_lengths.get)

        temp_nodes.remove(i)

        for v, weights_ij in adj_nodes[i].items():
            path_length[v] = min(path_length[v], path_length[i] + weights_ij)

    return path_length

nodes = [0, 1, 2, 3, 4, 5]
edges = {(0, 1): 1.0, (0, 2): 1.5, (0, 3): 2.0, (1, 3): 0.5,
            (1, 4): 2.5, (2, 3): 1.5, (3, 5): 1.0}
src_index = 0
print(dijkstra(nodes, edges, src_index))