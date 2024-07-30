class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class LinkedGraph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)
        return new_node

    def add_edge(self, node1, node2):
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    def bfs(self, start_node, target_value):
        visited = set()
        queue = [start_node]

        while queue:
            current_node = queue.pop(0)

            if current_node.value == target_value:
                return current_node

            visited.add(current_node)
            queue.extend(neighbor for neighbor in current_node.neighbors if neighbor not in visited)

        return None

    def dfs(self, start_node, target_value):
        visited = set()
        stack = [start_node]

        while stack:
            current_node = stack.pop()

            if current_node.value == target_value:
                return current_node

            visited.add(current_node)
            stack.extend(neighbor for neighbor in current_node.neighbors if neighbor not in visited)

        return None

    def all_paths(self, start_node, target_value, path=None):
        if path is None:
            path = []

        path = path + [start_node]

        if start_node.value == target_value:
            return [path]

        paths = []

        for neighbor in start_node.neighbors:
            if neighbor not in path:
                new_paths = self.all_paths(neighbor, target_value, path.copy())
                paths.extend(new_paths)

        return paths

# Test the implementation
my_graph = LinkedGraph()

# Add nodes
node_a = my_graph.add_node('A')
node_b = my_graph.add_node('B')
node_c = my_graph.add_node('C')
node_d = my_graph.add_node('D')

# Add edges
my_graph.add_edge(node_a, node_b)
my_graph.add_edge(node_b, node_c)
my_graph.add_edge(node_c, node_d)

# Test all_paths
result_all_paths = my_graph.all_paths(node_a, 'D')
print("All Paths:")
for path in result_all_paths:
    print([node.value for node in path])