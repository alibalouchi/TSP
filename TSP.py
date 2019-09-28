class TSP:
    def __init__(self, start_node, adjacency_matrix):
        self.start_node = start_node
        self.adjacency_matrix = adjacency_matrix

    def distance(self, node_start, node_end):
        return self.adjacency_matrix[node_start - 1][node_end - 1]
    def cost(self, nodes, initiate):
        result = []
        if len(nodes) < 2:
                return self.distance(self.start_node, nodes[0])
        else:
            for other_node in nodes:
                result.append(self.cost((nodes.pop(initiate)), other_node) + self.distance(other_node, initiate))
        return min(result)

test = TSP(1, [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
test2 = test.cost([1, 2, 3, 4], 1)
print (test2)