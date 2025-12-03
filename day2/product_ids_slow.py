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

def is_simple_invalid_str_id(id):
    half_length = int(len(id) / 2)
    return id[:half_length] == id[half_length:]

def is_invald_str_id(id):
    if len(id) == 1:
        return False
    if len(id) in [3, 5, 7]:
        return id[0]*len(id) == id
    elif len(id) == 2:
        return id[:1] == id[1:]
    elif len(id) == 4:
        return id[:2] == id[2:]
    elif len(id) == 6:
        return (id[:3] == id[3:] or
                id[:2]*3 == id)
    elif len(id) == 8:
        return id[:4] == id[4:]
    elif len(id) == 9:
        return id[:3]*3 == id
    elif len(id) == 10:
        return (id[:5] == id[5:] or
                id[:2]*5 == id)

invalid_id_total_part_1 = 0
invalid_id_total_part_2 = 0

id_ranges = data[0].split(",")
for id_range in id_ranges:
    start_id, end_id = [int(s) for s in id_range.split("-")]
    for id in range(start_id, end_id+1):
        if is_simple_invalid_str_id(str(id)):
            invalid_id_total_part_1 += id
        if is_invald_str_id(str(id)):
            invalid_id_total_part_2 += id

assert invalid_id_total_part_1 == 1227775554 if TESTDATA else True
assert invalid_id_total_part_2 == 4174379265 if TESTDATA else True

print("part 1:", invalid_id_total_part_1)
print("part 2:", invalid_id_total_part_2)
