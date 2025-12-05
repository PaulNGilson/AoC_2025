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

acquiring_ranges = True
id_ranges = []
food_ids = []

for line in data:
    if line == "":
        acquiring_ranges = False
    elif acquiring_ranges:
        id_ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
    else:
        food_ids.append(int(line))

id_ranges.sort()

more_to_try = True
while more_to_try:
    more_to_try = False
    for i in range(0, len(id_ranges)-1):
        id_range = id_ranges[i]
        id_range_next = id_ranges[i+1]
        if id_range_next[0] >= id_range[0] and id_range_next[0] <= id_range[1]:
            id_ranges[i] = (id_range[0], max(id_range[1], id_range_next[1]))
            id_ranges.pop(i+1)
            more_to_try = True
            break

fresh_food_ids = 0

for food_id in food_ids:
    for id_range in id_ranges:
        if food_id >= id_range[0] and food_id <= id_range[1]:
            fresh_food_ids += 1
            break

assert fresh_food_ids == 3 if TESTDATA else True
print("part 1:", fresh_food_ids)

all_fresh_food_ids = 0

for id_range in id_ranges:
    all_fresh_food_ids += (id_range[1] - id_range[0] + 1)

assert all_fresh_food_ids == 14 if TESTDATA else True
print("part 2:", all_fresh_food_ids)
