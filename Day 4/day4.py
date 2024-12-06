def read_file(filename):
    infile = open(filename, 'r')
    line_list = infile.readlines()
    new_line_list = []

    for line in line_list:
        new_line_list.append(line.strip('\n'))

    return new_line_list

# Check if row and column index within range of list of lists
def in_range(max_width, max_height, row, col):
    return row >= 0 and col >= 0 and row < max_width and col < max_height

# Part 1
def count_xmas(row, col, line_list):
    string = "XMAS"
    queue = []
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            # Skip iteration if on starting position
            if i == 0 and j == 0:
                continue
            
            # Append X for checking
            queue.append("X")

            # Add next 3 letters to string from starting position 
            for letter_index in range(1, 4):
                if in_range(len(line_list[0]), len(line_list), row + (i * letter_index), col + (j * letter_index)):
                    queue[len(queue) - 1] += line_list[row + (i * letter_index)][col + (j * letter_index)]

    # Loop through the queue and check if matches "XMAS" string
    while queue:
        check = queue.pop()    
        
        if check == string:
            count += 1
    
    return count

# Part 2
def count_mas(row, col, line_list):
    queue = []

    for i in range(-1, 2):
        for j in range(-1, 2):

            # Skip iteration if on 0 index
            if i == 0 or j == 0:
                continue
            
            queue.append("")

            # Add diagonals to the queue
            if in_range(len(line_list[0]), len(line_list), row + i, col + j):
                queue[len(queue) - 1] += line_list[row + i][col + j]


    string_list = []

    while queue:

        # Start and end of queue will always be the diagonals
        start = queue.pop()
        end = queue.pop(0)

        # Create string to check from start and end of queue
        string_list.append(start + "A" + end)
    
    # Check both diagonal strings if they are MAS forward or backward, if both are return True
    if (string_list[0] == "MAS" or string_list[0] == "SAM") and (string_list[1] == "MAS" or string_list[1] == "SAM"):
        return True
    
    return False

line_list = read_file('input.txt')
count = 0  

# Loop through file and when X is found, count the XMAS string in all 8 directions
for row, line in enumerate(line_list):
    for col, letter in enumerate(line):
        if letter == "X":
            count += count_xmas(row, col, line_list)

print("Part 1:", count)

# Part 2
mas_count = 0

for row, line in enumerate(line_list):
    for col, letter in enumerate(line):
        if letter == "A":
            if count_mas(row, col, line_list):
                mas_count += 1

print("Part 2:", mas_count)