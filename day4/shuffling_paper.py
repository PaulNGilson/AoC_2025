import sys

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

# pad the grid with dots, just to make handling edges easier
for i in range(0, len(data)):
    data[i] = "." + data[i] + "."
data = ["."*len(data[0])] + data + ["."*len(data[0])]

def accessible(x, y):
    neighbours = data[y-1][x-1:x+2] + data[y][x-1] + data[y][x+1] + data[y+1][x-1:x+2]
    return neighbours.count("@") < 4

accessible_count_part_1 = 0

for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        if data[y][x] == "@" and accessible(x, y):
            accessible_count_part_1 += 1

assert accessible_count_part_1 == 13 if TESTDATA else True
print("part 1:", accessible_count_part_1)

# part 2 begins

accessible_count_part_2 = 0
more_to_try = True

while more_to_try:
    more_to_try = False
    for y in range(1, len(data)-1):
        for x in range(1, len(data[0])-1):
            if data[y][x] == "@" and accessible(x, y):
                accessible_count_part_2 += 1
                data[y] = data[y][:x] + "." + data[y][x+1:]
                more_to_try = True

assert accessible_count_part_2 == 43 if TESTDATA else True
print("part 2:", accessible_count_part_2)
