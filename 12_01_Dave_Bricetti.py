from collections import defaultdict
import pprint
#import helpers

filepath = "12_01_Test1_Data.txt"

# using splitlines like this is good as it splits on the newline character
# which essentially removes it from each line during reading.
with open(filepath) as f:
    file_list = f.read().splitlines()

Targets = list[str]
TargetsBySource = dict[str, Targets]
paths: TargetsBySource = defaultdict(list)

for line in file_list:
    s, e = line.split('-')
    paths[s].append(e)
    paths[e].append(s)
print("paths_dict:", paths)

def dfs(path: list[str], visited: set[str], cave: str):
    if cave == 'end':
        solutions.append(path)
    else:
        if cave.islower():
            visited.add(cave)
        for next_cave in paths[cave]:
            if next_cave not in visited:
                dfs(path + [next_cave], set(visited), next_cave)

solutions: list[list[str]] = []
dfs(['start'], set(), 'start')
print("paths:\n")
pprint.pprint(solutions)
print("Number of Paths:", len(solutions))
