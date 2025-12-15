import sys
import copy

def open_input():
    filename = "input.txt"
    if TESTDATA:
        filename = "input_" + TESTDATA + ".txt"
    file = open(filename, "r")
    data_raw = file.readlines()
    file.close()
    data = []
    for line in data_raw:
        data.append(line.strip())
    return data

TESTDATA = None
if len(sys.argv) > 1:
    TESTDATA = sys.argv[1]

data = open_input()

connections = {}
for line in data:
    destinations = line.split(": ")[1].split()
    connections[line.split(": ")[0]] = destinations

paths = [["you"]]
routes = []
while paths:
    path = paths.pop()
    current = path[-1]
    for destination in connections[current]:
        if destination == "out":
            routes.append(path + [destination])
        else:
            paths.append(path + [destination])

assert len(routes) == 5 if TESTDATA else True
print("part 1:", len(routes))

# part 2 begins

paths_and_removals = {
    "total_paths": [],
    "no_dac": ["dac"],
    "no_fft": ["fft"],
    "no_fft_or_dac": ["fft", "dac"]
}
paths_counted = {}

for scenario in paths_and_removals:
    connections_copy = copy.deepcopy(connections)
    for to_remove in paths_and_removals[scenario]:
        del connections_copy[to_remove]
        for c in connections_copy:
            if to_remove in connections_copy[c]:
                connections_copy[c].remove(to_remove)

    backtracked = {"out": 1}
    while True:
        for connection in connections_copy:
            if connection not in backtracked and \
                ("out" in connections_copy[connection] or all(d in backtracked for d in connections_copy[connection])):
                backtracked[connection] = sum(backtracked[d] for d in connections_copy[connection] if d in backtracked)
        if "svr" in backtracked:
            break
    paths_counted[scenario] = backtracked["svr"]

print("part 2:", paths_counted["total_paths"] - paths_counted["no_dac"]  - paths_counted["no_fft"] + paths_counted["no_fft_or_dac"])
