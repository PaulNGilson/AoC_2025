import sys
import sympy
import itertools

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

# give ourselves enough symbols for the puzzle set
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o  = sympy.symbols('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o')
symbols = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]

button_presses_required_min_part_1 = 0
button_presses_required_min_part_2 = 0

for line in data:
    part_1_leds_s = line.split()[0][1:-1]
    part_2_joltage = [int(s) for s in line.split()[-1][1:-1].split(",")]
    button_combos = [[int(s) for s in s[1:-1].split(",")] for s in line.split()[1:-1]]

    # part 1
    combos = []
    leds = list(range(0, len(button_combos)))
    for i in range(1, len(button_combos)+1):
        for combo in itertools.combinations(leds, i):
            combos.append(combo)
    best_combo = ()
    for combo in combos:
        pressed = []
        for c in combo:
            pressed += button_combos[c]
        leds_s_achieved = ""
        for i in range(0, len(part_1_leds_s)):
            if pressed.count(i) % 2 == 0:
                leds_s_achieved += "."
            else:
                leds_s_achieved += "#"
        if leds_s_achieved == part_1_leds_s:
            best_combo = combo
            break
    button_presses_required_min_part_1 += len(best_combo)

    # part 2 begins
    # build list of linear equations: numbers of button presses, answers are target joltages
    equations = []
    for joltage_index in range(0, len(part_2_joltage)):
        eq_vals_to_add = []
        for b in range(0, len(button_combos)):
            if joltage_index in button_combos[b]:
                eq_vals_to_add.append(symbols[b])
        equations.append(sympy.Eq(sympy.core.add.Add(*eq_vals_to_add), part_2_joltage[joltage_index]))

    not_guessed_correct = True
    # initial guess is the minimum possible value of total button presses i.e. max joltage
    guess = max(part_2_joltage)
    while not_guessed_correct:
        # create one last equation which is the sum total of all button presses, with our guess as the answer
        eq_guess_total_presses = sympy.Eq(sympy.core.add.Add(*symbols[:len(button_combos)]), guess)
        q = sympy.linsolve(equations + [eq_guess_total_presses], symbols[:len(button_combos)])

        # check whether there is a solution at all (if not, we know our guess
        # was wrong) AND all integer presses are zero or higher to filter out
        # solutions we know are not possible
        if q:
            integer_presses = [q_part for q_part in list(q)[0] if isinstance(q_part, sympy.core.numbers.Integer)]
            if all(ip >= 0 for ip in integer_presses):
                possible_button_press_amounts = []
                free_symbols = list(q.free_symbols)
                for fs in free_symbols:
                    symbol_index = symbols.index(fs)
                    min_joltage = 10000
                    for pressed_led_index in button_combos[symbol_index]:
                        min_joltage = min(min_joltage, part_2_joltage[pressed_led_index])
                    possible_button_press_amounts += [list(range(min_joltage + 1))]

                symbol_guesses_combos = list(itertools.product(*possible_button_press_amounts))
                for symbol_guesses in symbol_guesses_combos:
                    q_copy = q.copy()
                    subs_list = []
                    for i in range(0, len(free_symbols)):
                        subs_list.append([free_symbols[i], symbol_guesses[i]])
                    q_copy = q_copy.subs(subs_list)
                    q_copy = list(q_copy)[0]
                    # all the button press values need to be positive integers for us to have found the answer
                    if all(isinstance(bps, sympy.core.numbers.Integer) and bps >= 0 for bps in q_copy):
                        button_presses_required_min_part_2 += guess
                        not_guessed_correct = False
                        break
        guess += 1

print("part 1:", button_presses_required_min_part_1)
print("part 2:", button_presses_required_min_part_2)
