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

def lookup_values(length):
    if length == 1:
        return []
    if length in [3, 5, 7]:
        return [(1, length)]
    elif length == 2:
        return [(1, 2)]
    elif length == 4:
        return [(2, 2)]
    elif length == 6:
        return [(2, 3), (3, 2)]
    elif length == 8:
        return [(4, 2)]
    elif length == 9:
        return [(3, 3)]
    elif length == 10:
        return [(2, 5), (5, 2)]

def generate_invalid_ids(start_s, end_s, length, repetitions):
    start = int(start_s)
    end = int(end_s)
    ids = []
    repeater = start_s[:length]
    if int(repeater*repetitions) >= start and int(repeater*repetitions) <= end:
        ids.append(repeater*repetitions)
    while True:
        repeater = str(int(repeater) + 1)
        if int(repeater*repetitions) <= end:
            ids.append(repeater*repetitions)
        else:
            break
    return ids

invalid_ids_set_part_1 = set()
invalid_ids_set_part_2 = set()

id_ranges = data[0].split(",")
for id_range in id_ranges:
    start_id_s, end_id_s = id_range.split("-")
    if len(start_id_s) == len(end_id_s):
        constrained_ranges = [(start_id_s, end_id_s)]
    else:
        constrained_ranges = [(start_id_s, "9"*len(start_id_s)), ("1"+"0"*len(start_id_s), end_id_s)]
    for constrained_range in constrained_ranges:
        combinations = lookup_values(len(constrained_range[0]))
        for combination in combinations:
            for invalid_id in generate_invalid_ids(constrained_range[0], constrained_range[1], combination[0], combination[1]):
                if combination[1] == 2:
                    invalid_ids_set_part_1.add(int(invalid_id))
                invalid_ids_set_part_2.add(int(invalid_id))

assert sum(invalid_ids_set_part_1) == 1227775554 if TESTDATA else True
assert sum(invalid_ids_set_part_2) == 4174379265 if TESTDATA else True

print("part 1:", sum(invalid_ids_set_part_1))
print("part 2:", sum(invalid_ids_set_part_2))
