import sys
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

suitable_regions = 0

for line in data:
    if "x" in line:
        max_number_3x3_spaces = math.prod(math.floor(int(dim)/3) for dim in line.split(": ")[0].split("x"))
        present_counts = sum(int(count) for count in line.split(": ")[1].split(" "))
        if present_counts <= max_number_3x3_spaces:
            suitable_regions += 1
        else:
            pass # we don't want to know what would've happened here, if the data had been different...

print("part 1:", suitable_regions)
