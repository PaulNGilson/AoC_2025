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

position = 50
zeroes_reached = 0 # part 1
zeroes_passed = 0  # part 2

for rotation in data:
    direction, amount = rotation[0], int(rotation[1:])
    if direction == "R":
        position_new_value = position + amount
    else:
        position_new_value = position - amount
        if position_new_value <= 0 and position != 0:
            zeroes_passed += 1
    zeroes_passed += abs(int(position_new_value/100))
    position = position_new_value % 100
    if position == 0:
        zeroes_reached += 1

print("part 1:", zeroes_reached)
print("part 2:", zeroes_passed)

assert zeroes_reached == 3 if TESTDATA else True
assert zeroes_passed == 6 if TESTDATA else True
