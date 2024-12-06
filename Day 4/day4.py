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
    
line_list = read_file('input.txt')
count = 0  

# Loop through file and when X is found, count the XMAS string in all 8 directions
for row, line in enumerate(line_list):
    for col, letter in enumerate(line):
        if letter == "X":
            count += count_xmas(row, col, line_list)

print("Part 1:", count)