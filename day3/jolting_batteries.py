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

def fetch_next_best(remaining_bank, length_required):
    if length_required == 1:
        return max(list(remaining_bank))
    cannot_use_size = length_required - 1
    return max(list(remaining_bank)[:-cannot_use_size])

def calculate_joltage(batteries_required):
    output_joltage_total = 0
    for bank in data:
        batteries_left = batteries_required
        bank_joltage = ""
        while batteries_left > 0:
            dig = fetch_next_best(bank, batteries_left)
            bank_joltage += dig
            batteries_left -= 1
            bank = bank[bank.index(dig)+1:]
        output_joltage_total += int(bank_joltage)
    return output_joltage_total

print("part 1:", calculate_joltage(2))
print("part 2:", calculate_joltage(12))

# assert calculate_joltage(2) == 357 if TESTDATA else True
# assert calculate_joltage(12) == 3121910778619 if TESTDATA else True
