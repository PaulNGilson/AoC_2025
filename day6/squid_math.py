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
        data.append(line) # don't strip spaces here, they are important
    return data

TESTDATA = None
if len(sys.argv) > 1:
    TESTDATA = sys.argv[1]

data = open_input()

input_info = []
for line in data:
    input_info.append(line.split())

grand_total_part_1 = 0

for calculation_index in range(0, len(input_info[0])):
    operation = input_info[-1][calculation_index]
    numbers = []
    for i in range(0, len(data)-1):
        numbers.append(int(input_info[i][calculation_index]))
    if operation == "+":
        grand_total_part_1 += sum(numbers)
    else:
        grand_total_part_1 += math.prod(numbers)

assert grand_total_part_1 == 4277556 if TESTDATA else True
print("part 1:", grand_total_part_1)

# part 2 begins

grand_total_part_2 = 0
numbers = []

for col_index in range(0, len(data[0])):
    if numbers == []:
        operation = data[-1][col_index]
    number = ""
    for row_index in range(0, len(data)-1):
        number += data[row_index][col_index]
    if number == " "*(len(data)-1) or number == "\n"*(len(data)-1):
        if operation == "+":
            grand_total_part_2 += sum(numbers)
        else:
            grand_total_part_2 += math.prod(numbers)
        numbers = []
    else:
        numbers.append(int(number))

assert grand_total_part_2 == 3263827 if TESTDATA else True
print("part 2:", grand_total_part_2)
