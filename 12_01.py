import sys
print(sys.version)
print(sys.executable)

filepath = "12_01_Test1_Data.txt"

# using splitlines like this is good as it splits on the newline character
# which essentially removes it from each line during reading.
with open(filepath) as f:
    file_list = f.read().splitlines()

print("file_list:", file_list)

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

print("nodes:", nodes)


# Find children of each node and add to a list:
for node in nodes:
    print("\ncurrent node being checked:", node)
    children = []
    for pair in file_list:
        partitioned_string = pair.partition("-")
        print("Partitioned String: ", partitioned_string)
        if partitioned_string[0] != node and partitioned_string[2] == node:
            children.append(partitioned_string[0])
            print("child appended: ", partitioned_string[0])
        else:
            if partitioned_string[2] != node and partitioned_string[0] == node:
                children.append(partitioned_string[2])
                print("child appended: ", partitioned_string[2])

    print("node:",node, "\n children:", children, "\n")

    # Now add the node and chlidren to an adjacency list dictionary:
    graph_dict[node] = children
    print("graph_dict so far:", graph_dict)

# Now do Depth First Search of Graph:
visited = [] # to keep track of visited nodes
current_path = []

def dfs(visited, graph, node, destination_node):
    # If end is reached, save current path and backtrack.....
        if node == destination_node:
            current_path.append(node)
            visited.append(node)
            print("current path is currently:", current_path)
            return(current_path)

        print("node being visited:", node)
        # Don't add to visited if it's an upper case letter:
        if not node.isupper():
            visited.append(node)
        # Add to 'current path no matter what'
        current_path.append(node)
        # print("current path is currently:", current_path)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(visited, graph, neighbour, destination_node)

                return(current_path)

#Driver code for dfs function:
dfs(visited, graph_dict, "start", "end")
print("current path:", current_path)
