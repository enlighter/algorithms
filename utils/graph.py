class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found is None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found is None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        ret = []
        for edge in self.edges:
            ret.append((edge.value, edge.node_from.value, edge.node_to.value))
        return ret

    def __find_node(self, index):
        for node in self.nodes:
            if node.value == index:
                return node

    def __find_max_node(self):
        max_node = None
        for node in self.nodes:
            if not max_node:
                max_node = node.value
                continue
            if node.value > max_node:
                max_node = node.value
        return max_node

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        ret = []
        for i in range(self.__find_max_node() + 1):
            node = self.__find_node(i)
            if node is None:
                # print('node no. {}: {}'.format(i, None))
                ret.append(None)
                continue
            # print('node no. {}: {}'.format(i, node.value))
            adjacents = []
            for edge in node.edges:
                if edge.node_to.value == node.value:
                    # these are incoming edges not outgoing edges
                    continue
                adjacents.append((edge.node_to.value, edge.value))
            if adjacents:
                ret.append(adjacents)
            else:
                ret.append(None)
        return ret

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        matrix = []
        for i in range(self.__find_max_node() + 1):
            matrix.append([0 for j in range(self.__find_max_node() + 1)])
        for edge in self.edges:
            matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return matrix


if __name__ == '__main__':
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)
    # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print(graph.get_edge_list())
    # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    print(graph.get_adjacency_list())
    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
    print(graph.get_adjacency_matrix())