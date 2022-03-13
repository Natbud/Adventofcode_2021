import sys
import pprint
print(sys.version)
print(sys.executable)

filepath = "12_01_Test1_Data.txt"

# using splitlines like this is good as it splits on the newline character
# which essentially removes it from each line during reading.
with open(filepath) as f:
    file_list = f.read().splitlines()

# print("file_list:", file_list)

# Define graph:
graph_dict = {}

# Add all 'nodes' to a Node list:
nodes = []

for pair in file_list:
    partitioned_string = pair.partition("-")
    if partitioned_string[0] not in nodes:
        nodes.append(partitioned_string[0])
    if partitioned_string[2] not in nodes:
        nodes.append(partitioned_string[2])

# print("nodes:", nodes)


# Find children of each node and add to a list:
for node in nodes:
    # print("\ncurrent node being checked:", node)
    children = []
    for pair in file_list:
        partitioned_string = pair.partition("-")
        # print("Partitioned String: ", partitioned_string)
        if partitioned_string[0] != node and partitioned_string[2] == node:
            children.append(partitioned_string[0])
            # print("child appended: ", partitioned_string[0])
        else:
            if partitioned_string[2] != node and partitioned_string[0] == node:
                children.append(partitioned_string[2])
                # print("child appended: ", partitioned_string[2])

    # print("node:",node, "\n children:", children, "\n")

    # Now add the node and chlidren to an adjacency list dictionary:
    graph_dict[node] = children
    # print("graph_dict so far:", graph_dict)
print("graph_dict:\n")
pprint.pprint(graph_dict)
print("\n\n")

# Now do Depth First Search using recursion:
visited = [] # to keep track of visited nodes
# path = []
solutions = []

def dfs(path: list[str], visited, graph, node, destination_node):

    # If end is reached,....this is my 'BASE
    # CASE where there is only one path between a node and itself so return 1.

        if node == destination_node:
            solutions.append(path)
        else:
            # Don't add to "visited" if it's an upper case letter:
            if node.islower():
                visited.add(node)

            # Now visit all neighbours recursively
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(path + [neighbour], set(visited), graph, neighbour, destination_node)


#Driver code for dfs function:
dfs(['start'], set(), graph_dict, "start", "end")
for solution in solutions:
    print(solution)
print("Number of Paths:", len(solutions))
