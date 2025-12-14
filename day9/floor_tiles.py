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

tile_coords = []

for line in data:
    tile_coords.append((int(line.split(",")[0]), int(line.split(",")[1])))

carpet_sizes = []

for i in range(0, len(tile_coords)-1):
    for j in range(i+1, len(tile_coords)):
        x_distance = abs(tile_coords[i][0] - tile_coords[j][0]) + 1
        y_distance = abs(tile_coords[i][1] - tile_coords[j][1]) + 1
        carpet_sizes.append((x_distance * y_distance, tile_coords[i], tile_coords[j]))
carpet_sizes.sort()

assert carpet_sizes[-1][0] == 50 if TESTDATA else True
print("part 1:", carpet_sizes[-1][0])

corner_coords_left = []
corner_coords_right = []

def get_direction(tile_from, tile_to):
    if tile_to[1] == tile_from[1]:
        if tile_to[0] > tile_from[0]:
            return "E"
        else:
            return "W"
    else:
        if tile_to[1] > tile_from[1]:
            return "S"
        else:
            return "N"

tile_coords += tile_coords[:2] # wrap so we can record all the edges and corners

direction = get_direction(tile_coords[0], tile_coords[1]) # initial direction

for i in range(1, len(tile_coords)-1):
    new_direction = get_direction(tile_coords[i], tile_coords[i+1])
    if direction == "E" and new_direction == "S": # right turn
        corner_coords_right.append((tile_coords[i][0]+1, tile_coords[i][1]))
        corner_coords_right.append((tile_coords[i][0], tile_coords[i][1]-1))
    elif direction == "W" and new_direction == "N": # right turn
        corner_coords_right.append((tile_coords[i][0]-1, tile_coords[i][1]))
        corner_coords_right.append((tile_coords[i][0], tile_coords[i][1]+1))
    elif direction == "N" and new_direction == "E": # right turn
        corner_coords_right.append((tile_coords[i][0], tile_coords[i][1]-1))
        corner_coords_right.append((tile_coords[i][0]-1, tile_coords[i][1]))
    elif direction == "S" and new_direction == "W": # right turn
        corner_coords_right.append((tile_coords[i][0], tile_coords[i][1]+1))
        corner_coords_right.append((tile_coords[i][0]+1, tile_coords[i][1]))
    elif direction == "N" and new_direction == "W": # left turn
        corner_coords_left.append((tile_coords[i][0], tile_coords[i][1]-1))
        corner_coords_left.append((tile_coords[i][0]+1, tile_coords[i][1]))
    elif direction == "S" and new_direction == "E": # left turn
        corner_coords_left.append((tile_coords[i][0], tile_coords[i][1]+1))
        corner_coords_left.append((tile_coords[i][0]-1, tile_coords[i][1]))
    elif direction == "E" and new_direction == "N": # left turn
        corner_coords_left.append((tile_coords[i][0]+1, tile_coords[i][1]))
        corner_coords_left.append((tile_coords[i][0], tile_coords[i][1]+1))
    else: # direction == "W" and new_direction == "S": # left turn
        corner_coords_left.append((tile_coords[i][0]-1, tile_coords[i][1]))
        corner_coords_left.append((tile_coords[i][0], tile_coords[i][1]-1))
    direction = new_direction

if len(corner_coords_right) > len(corner_coords_left):
    corner_coords_outside = corner_coords_right
else:
    corner_coords_outside = corner_coords_left

tile_coords.pop() # done looking at corners, just looking at edges now so only wrap one coord

still_looking = True

while still_looking:
    next_carpet_size, tile_i, tile_j = carpet_sizes.pop()
    edge_hor_a = ((min(tile_i[0], tile_j[0]), tile_i[1]), (max(tile_i[0], tile_j[0]), tile_i[1]))
    edge_hor_b = ((min(tile_i[0], tile_j[0]), tile_j[1]), (max(tile_i[0], tile_j[0]), tile_j[1]))
    edge_ver_a = ((tile_i[0], min(tile_i[1], tile_j[1])), (tile_i[0], max(tile_i[1], tile_j[1])))
    edge_ver_b = ((tile_j[0], min(tile_i[1], tile_j[1])), (tile_j[0], max(tile_i[1], tile_j[1])))
    unbroken_lines = True
    for i in range(0, len(tile_coords)-1):
        tile_i = tile_coords[i]
        tile_j = tile_coords[i+1]
        if tile_i[0] == tile_j[0]: # vertical line
            if (edge_hor_a[0][0] < tile_i[0] and tile_i[0] < edge_hor_a[1][0]) and \
                (min(tile_i[1], tile_j[1]) < edge_hor_a[0][1] and edge_hor_a[0][1] < max(tile_i[1], tile_j[1])):
                unbroken_lines = False
                break
            if (edge_hor_b[0][0] < tile_i[0] and tile_i[0] < edge_hor_b[1][0]) and \
                (min(tile_i[1], tile_j[1]) < edge_hor_b[0][1] and edge_hor_b[0][1] < max(tile_i[1], tile_j[1])):
                unbroken_lines = False
                break
        else: # horizontal line
            if (min(tile_i[0], tile_j[0]) < edge_ver_a[0][0] and edge_ver_a[0][0] < max(tile_i[0], tile_j[0])) and \
                (edge_ver_a[0][1] < tile_i[1] and tile_i[1] < edge_ver_a[1][1]):
                unbroken_lines = False
                break
            if (min(tile_i[0], tile_j[0]) < edge_ver_b[0][0] and edge_ver_b[0][0] < max(tile_i[0], tile_j[0])) and \
                (edge_ver_b[0][1] < tile_i[1] and tile_i[1] < edge_ver_b[1][1]):
                unbroken_lines = False
                break
    if unbroken_lines:
        for corner_coord in corner_coords_outside:
            if corner_coord[0] == edge_ver_a[0][0]:
                if edge_ver_a[0][1] < corner_coord[1] and corner_coord[1] < edge_ver_a[1][1]:
                    unbroken_lines = False
                    break
            if corner_coord[0] == edge_ver_b[0][0]:
                if edge_ver_b[0][1] < corner_coord[1] and corner_coord[1] < edge_ver_b[1][1]:
                    unbroken_lines = False
                    break
            if corner_coord[1] == edge_hor_a[0][1]:
                if edge_hor_a[0][0] < corner_coord[0] and corner_coord[0] < edge_hor_a[1][0]:
                    unbroken_lines = False
                    break
            if corner_coord[1] == edge_hor_b[0][1]:
                if edge_hor_b[0][0] < corner_coord[0] and corner_coord[0] < edge_hor_b[1][0]:
                    unbroken_lines = False
                    break
    if unbroken_lines:
        still_looking = False

assert next_carpet_size == 24 if TESTDATA else True
print("part 2:", next_carpet_size)
