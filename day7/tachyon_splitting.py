import sys
from collections import defaultdict

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

beams = [data[0].index("S")]
split_count = 0

for row in data[1:]:
    splitters = [i for i, c in enumerate(row) if c == "^"]
    new_beams = []
    splitters_hit = []
    for beam in beams:
        if beam in splitters:
            new_beams.append(beam-1)
            new_beams.append(beam+1)
            splitters_hit.append(beam)
        else:
            new_beams.append(beam)
    beams = list(set(new_beams))
    split_count += len(set(splitters_hit))

assert split_count == 21 if TESTDATA else True
print("part 1:", split_count)

# part 2 begins

beams = defaultdict(int)
beams[data[0].index("S")] = 1 # index: number_of_beams/timelines)

for row in data[1:]:
    splitters = [i for i, c in enumerate(row) if c == "^"]
    new_beams = defaultdict(int)
    for beam in beams:
        if beam in splitters:
            new_beams[beam-1] += beams[beam]
            new_beams[beam+1] += beams[beam]
        else:
            new_beams[beam] += beams[beam]
    beams = new_beams

assert sum(beams.values()) == 40 if TESTDATA else True
print("part 2:", sum(beams.values()))
