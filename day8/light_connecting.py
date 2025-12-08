import sys
import numpy
import math

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

junction_boxes = []
lookup = {}
circuits = {}
i = 0
for line in data:
    coords = [int(i) for i in line.split(",")]
    junction_boxes.append(numpy.array(coords))
    lookup[i] = coords
    circuits[i] = set([i])
    i += 1

number_connections = 100 if TESTDATA else 10000 # set way over the number we are likely to need to connect
shortest_connections = [(10000000, [],[])] * number_connections
for i in range(0, len(junction_boxes)-1):
    for j in range(i+1, len(junction_boxes)):
        distance = numpy.linalg.norm(junction_boxes[j] - junction_boxes[i])
        if distance < shortest_connections[-1][0]:
            shortest_connections[-1] = (distance, junction_boxes[i], junction_boxes[j])
            shortest_connections.sort()

connections = []
for shortest_connection in shortest_connections:
    connections.append((list(lookup.values()).index(shortest_connection[1].tolist()),
                        list(lookup.values()).index(shortest_connection[2].tolist())))

connected_count = 10 if TESTDATA else 1000
for connection in connections:
    for k in circuits.keys():
        if connection[0] in circuits[k]:
            i = k
        if connection[1] in circuits[k]:
            j = k
    if i != j:
        circuits[i].update(circuits.pop(j))

    connected_count -= 1
    if connected_count == 0:
        junction_circuit_sizes = sorted([len(junctions) for junctions in circuits.values()])
        assert math.prod(junction_circuit_sizes[-3:]) == 40 if TESTDATA else True
        print("part 1:", math.prod(junction_circuit_sizes[-3:]))

    elif len(circuits) == 1:
        assert lookup[connection[0]][0] * lookup[connection[1]][0] == 25272 if TESTDATA else True
        print("part 2:", lookup[connection[0]][0] * lookup[connection[1]][0])
        break
