def read_file(filename):
    infile = open(filename, 'r')
    line_list = infile.readlines()
    new_list = []

    for line in line_list:
        if line == '\n':
            break

        new_list.append(line.strip('\n'))


    return new_list

# Input
guard_map = read_file('input.txt')

# y, x order
directions = {
    '^': [-1, 0],
    '>': [0, 1],
    'v': [1, 0],
    '<': [0, -1]
}

# Rotating clockwise
rotation = ['^', '>', 'v', '<']

# Starting direction
current = '^'

row_count = len(guard_map)
col_count = len(guard_map[0])
x = -1
y = -1
visited = []

for row in guard_map:
    if current in row:
        x = row.index(current)
        y = guard_map.index(row)

next_x = x + directions[current][1]
next_y = y + directions[current][0]

while next_x >= 0 and next_x < col_count and next_y >= 0 and next_y < row_count:
    if [x, y] not in visited:
        visited.append([x, y])
    
    if guard_map[next_y][next_x] == '#':
        start_x = x
        start_y = y
        next_index = (rotation.index(current) + 1) % 4
        current = rotation[next_index]
        next_x = x + directions[current][1]
        next_y = y + directions[current][0]
        
    x = next_x
    y = next_y
    next_x = x + directions[current][1]
    next_y = y + directions[current][0]

if [x, y] not in visited:
    visited.append([x, y])

print(len(visited))
