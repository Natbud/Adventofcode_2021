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
    print("\ncurrent node being checked: ", node)
    children = []
    for pair in file_list:
        partitioned_string = pair.partition("-")
        print("Partitioned String: ", partitioned_string)
        if partitioned_string[0] is not node and partitioned_string[2] is node:
            children.append(partitioned_string[0])
            print("child appended: ", partitioned_string[0])
        else:
            if partitioned_string[2] is not node and partitioned_string[0] is node:
                children.append(partitioned_string[2])
                print("child appended: ", partitioned_string[2])

    print("node: ", node, "\n children:", children, "\n")
