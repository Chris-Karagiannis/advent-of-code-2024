def read_file(filename):
    infile = open(filename, 'r')
    line_list = infile.readlines()
    priority_list = []

    for line in line_list:
        if line == '\n':
            break

        priority_list.append(line.strip('\n').split('|'))


    return priority_list

def read_page_numbers(filename, start):
    infile = open(filename, 'r')
    line_list = infile.readlines()
    new_list = []

    for i in range(start, len(line_list)):
        new_list.append(line_list[i].strip('\n').split(','))

    return new_list

priority_list = sorted(read_file('input.txt'), key=lambda priority: priority[0])
page_numbers = read_page_numbers('input.txt', len(priority_list) + 1)
priority = {}

# Entrys to dictionary with all the numbers they have priority over in a list
for entry in priority_list:
    if entry[0] not in priority:
        priority[entry[0]] = []
    
    priority[entry[0]].append(entry[1])

# Add lines to list if priority is correct
valid = []

invalid = []

for line in page_numbers:
    for i in range(1, len(line)):

        # Checks if the index prior is in the list
        if line[i - 1] in priority:

            # Then checks if the current index value is not in the priority dictionary of the previous index
            # If true, means the previous index doesn't have priority therefore not valid
            if line[i] not in priority[line[i - 1]]:
                invalid.append(line)
                break
        
        # If previous value is not in the priority dictionary means it has no priority therefore not valid
        else:
            invalid.append(line)
            break
        
        # If get to the end of the loop without breaks, means line is valid and can be add to list
        if i == len(line) - 1:
            valid.append(line)


# Add up middle index values
total = 0

for line in valid:
    line_length = len(line)
    middle_index = (line_length) // 2
    total += int(line[middle_index])

print("Part 1:", total)



# Part 2
for line in invalid:

    i = 1

    # Sort the invalid list based on priority
    while i < len(line):
        if line[i - 1] in priority:
            if line[i] not in priority[line[i - 1]]:
                line[i], line[i - 1] = line[i - 1], line[i]
                i = 1
                continue
        else:
            line[i], line[i - 1] = line[i - 1], line[i]
            i = 1
            continue
        
        i += 1
       
# Add up middle index values
invalid_total = 0

for line in invalid:
    line_length = len(line)
    middle_index = (line_length) // 2
    invalid_total += int(line[middle_index])        
    
print("Part 2:", invalid_total)

